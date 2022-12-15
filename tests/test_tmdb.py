import tmdb_client
from unittest.mock import Mock




def test_get_poster_url_ises_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = "w342/"
    poster_url = tmdb_client.get_poster_url(poster_api_path,expected_default_size)

    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"



def test_get_movies_list(monkeypatch):
    mock_movies_list = ["movie 1", "movie 2"]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type='popular')
    assert movies_list == mock_movies_list




def test_get_single_movie(monkeypatch):
    """test - sprawdza czy pobiera pojedynczy film"""
    mock_movie = 'Kiler'
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie = tmdb_client.get_single_movie(1)
    assert movie == mock_movie


def test_default_movie_id():
    """test - sprawdza, czy endpoint tworzy sie właściwy"""
    default_movie_id = "messi10"
    endpoint = f"https://api.themoviedb.org/3/movie/{default_movie_id}"
    assert endpoint == "https://api.themoviedb.org/3/movie/messi10"



def test_get_single_movie_images(monkeypatch):
    """test - sprawdza, czy funkcja pobiera zdjecia"""
    mock_images = ['img1.jpg', 'img2.jpg']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_images
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    images = tmdb_client.get_single_movie_images(1)
    assert images == mock_images




def test_get_single_movie_cast(monkeypatch):
    """test - sprawdza, czy funkcja pobiera obsade"""
    mock_casts =   {'cast':['actor1', 'actor2']}
    requests_mock = Mock()
    response = requests_mock.return_value 
    response.json.return_value = mock_casts
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    casts = tmdb_client.get_single_movie_cast(1)
    assert casts == mock_casts['cast']


