import datetime
from googleapiclient.http import HttpMock
import pytest

from geevent import GeEvent, GeeProject


@pytest.fixture
def gcal_data():
    http = HttpMock('mock.json', {'status': '200'})
    api_key = 'your_api_key'
    service = build('calendar', 'v3', http=http, developerKey=api_key)

    return service.events()


class TestGeevent(object):
    def test_init(self):
        geevent = GeEvent("01",
                          "Summary",
                          "2018-12-10T17:30:00-08:00",
                          "2018-12-10T18:30:00-08:00")
        assert geevent
        assert type(geevent.duration) is datetime.timedelta


class TestGeeProject(object):
    def test_init(self):
        geeproject = GeeProject("Work")

        assert geeproject
        assert geeproject.project_id == "Work"
