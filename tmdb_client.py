import requests
import random
import os

api_token = os.environ.get("TMDB_API_TOKEN", "")


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movies_list(list_type):
    #pobiera listy z filmami, w prypadku wpisania zlej listy zwraca liste popular
    try:
        return call_tmdb_api(f"movie/{list_type}")
    except requests.exceptions.HTTPError:
        return call_tmdb_api(f"movie/popular")


def get_poster_url(poster_path, size="w342"):
    #tworzy adresy url zdjec
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_path}"


def get_movies(list_type, how_many):
    # pobiera wybrana ilosc filmow na strone glowna
    data = get_movies_list(list_type)
    random.shuffle(data['results'])
    return data['results'][:how_many]


def get_single_movie(movie_id):
    # pobiera szczegoly danego filmu
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id):
    # pobiera info o aktorach
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_single_movie_images(movie_id):
    # pobiera dodatkowe zdjecia z filmow
    return call_tmdb_api(f"movie/{movie_id}/images")


def search(search_query):
    #wyszukuje filmy
    base_url = "https://api.themoviedb.org/3/"   
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    endpoint = f"{base_url}search/movie/?query={search_query}"

    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']


def get_airing_today():
    """pobiera seriale emitowane dzisiejszego dnia"""
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']


