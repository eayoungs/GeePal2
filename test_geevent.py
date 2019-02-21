import datetime
from googleapiclient.discovery import build
from googleapiclient.http import HttpMock
import pytest

from geevent import GeEvent, GeeProject


@pytest.fixture(scope="module")
def gcal_mock():
    http = HttpMock('calendar-discovery.json', {'status': '200'})
    api_key = 'your_api_key'
    service = build('calendar', 'v3', http=http, developerKey=api_key)

    return service


@pytest.fixture(scope="module")
def gcal_geevent(gcal_mock):
    pass


class TestGeEvent(object):
    def test_init(self, gcal_mock):
        pass


class TestGeProject(object):
    def test_init(self):
        pass

    def test_add(self, gcal_geevent):
        pass

service = gcal_mock()
print(service.events)
