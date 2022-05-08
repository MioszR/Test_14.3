import random
from flask import Flask, render_template, request
import tmbd_client

app = Flask(__name__)

type_list = ["popular", "now_playing", "top_rated", "upcoming"]


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    if selected_list not in type_list:
        selected_list = "popular"
    movies = tmbd_client.get_movies(how_many=12, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, new_list=type_list)

@app.context_processor
def utility_processor():
    def tmbd_image_url(path, size):
        return tmbd_client.get_poster_url(path, size)
    return {"tmbd_image_url": tmbd_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmbd_client.get_single_movie(movie_id)
    cast = tmbd_client.get_single_movie_cast(movie_id)
    movie_images = tmbd_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)

if __name__ == '__main__':
    app.run(debug=True)