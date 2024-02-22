import pytest
from app2 import app, fetch_match_details_from_api

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200

def test_index_post(client, monkeypatch):
    mock_response = [{'match': 'details'}]

    def mock_get(url):
        return mock_response

    monkeypatch.setattr('app2.requests.get', mock_get)

    response = client.post('/', data={'date': '2024-02-11', 'league': '168'})
    assert response.status_code == 200

def test_match_details(client, monkeypatch):
    mock_response = [{'match': 'details'}]

    def mock_get(url):
        return mock_response

    monkeypatch.setattr('app2.requests.get', mock_get)

    response = client.get('/match_details/123')
    assert response.status_code == 200
