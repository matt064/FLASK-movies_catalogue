import requests
import random

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NTkxNjlmMjZjNDc1YTZiZDlhOWFjNDMyNjZkMGE5ZiIsInN1YiI6IjYzNzRhZDM4ZDdkY2QyMDA3ZjdjOTE3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oVKhhiF6Y-4c8GE9rm50J8_W0tTNQnF85_0yJffThsc"

def get_movies_list(list_type):
    #pobiera listy z filmami, w prypadku wpisania zlej listy zwraca liste popular
    try:
        endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
        headers = {
        "Authorization": f"Bearer {api_token}"
        }    
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status() #dzieki temu operujemy na poprawnych danych
        return response.json()
    except requests.exceptions.HTTPError:
        endpoint = f"https://api.themoviedb.org/3/movie/popular"
        headers = {
        "Authorization": f"Bearer {api_token}"
        }    
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status() 
        return response.json()


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
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


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
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



# do wgladu danych
# data_movie = get_single_movie_images(829280)

# print(data_movie)




# for movie in data_movie['results']:
#     print (movie)

