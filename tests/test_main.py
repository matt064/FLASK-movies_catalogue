from main import app
from unittest.mock import Mock
import pytest

def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')



@pytest.mark.parametrize('list_type, status_code',(
    ('now_playing', 200),
    ('popular', 200),    
    ('top_rated', 200),
    ('upcoming', 200)
))
def test_list_type(list_type, status_code, monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get(f'/?list_type={list_type}')
       assert response.status_code == status_code
       api_mock.assert_called_with(f'movie/{list_type}')

