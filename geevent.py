import iso8601


class GeEvent:
    def __init__(self, geevent_id, summary, start, end):
        self.geevent_id = geevent_id
        self.summary = summary
        self.start = start
        self.end = end
        try:
            self.duration = iso8601.parse_date(self.end) - iso8601.parse_date(self.start)
        except TypeError as e:
            return e
