from mock import patch
from api.main import app
from fastapi.testclient import TestClient
import pytest
from api.service.tweet_service import TweetService
client = TestClient(app)

def test_api_is_up():
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.json() == { 'body' : 'I am free!!!' }

@pytest.fixture()
def mocked_service():
    with patch('api.service.tweet_service.TweetService.get_total_incidence_between_dates', return_value=3765):
        service = TweetService()
        yield service
        
def test_total_incidence_between_dates(mocked_service):
    response = client.get('/total_incidence_between_dates')

    assert response.status_code == 200
    assert response.json() == { 'body' : 3765 }

