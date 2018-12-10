import datetime

from geevent import GeEvent


def test_init():
    geevent = GeEvent("Summary",
                      "2018-12-10T17:30:00-08:00",
                      "2018-12-10T18:30:00-08:00")
    assert geevent
    assert type(geevent.duration) is datetime.timedelta
