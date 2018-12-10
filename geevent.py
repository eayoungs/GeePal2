import iso8601


class GeEvent:
    def __init__(self, summary, start, end):
        self.summary = summary
        self.start = start
        self.end = end
        try:
            self.duration = iso8601.parse_date(self.end) - iso8601.parse_date(self.start)
        except TypeError as e:
            return e
