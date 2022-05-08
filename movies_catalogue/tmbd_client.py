import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YTA2ZDNiYjJhMDUxYWZmM2M2YjMzMWQzNTdkMmEzNCIsInN1YiI6IjYyNWVlYmM0ZDFhODkzMDA2NzBmZDBmMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fqOABWxDGZdGlPnsAgKZIT6AG3JoC2cIqSPFLpE67Ks"

def get_pop():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def call_tmbd_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_movies_list(list_type):
    return call_tmbd_api(f"movie/{list_type}")

