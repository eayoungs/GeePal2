import pytest

from geevent import GeEvent


def test_init():
    assert GeEvent("Summary",
                   "2018-12-10T17:30:00-08:00",
                   "2018-12-10T18:30:00-08:00")
