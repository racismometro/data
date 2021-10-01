
from mock import patch
from api.main import app
from fastapi.testclient import TestClient
from api.service.tweet_service import TweetService

import pytest

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
        
@patch('configparser.RawConfigParser.getboolean')
def test_total_incidence_between_dates_toggle_on(mocked_getboolean, mocked_service):
    mocked_getboolean.return_value = True
    
    response = client.get('/total_incidence_between_dates/start-date=06-01-2021&end-date=06-31-2021')

    assert response.status_code == 200
    assert response.json() == { 'body' : 3765 }

@patch('configparser.RawConfigParser.getboolean')
def test_total_incidence_between_dates_toggle_off(mocked_getboolean, mocked_service):
    mocked_getboolean.return_value = False

    response = client.get('/total_incidence_between_dates/start-date=06-01-2021&end-date=06-31-2021')

    assert response.status_code == 200
    assert response.json() == { 'body' : 'feature is disabled' }