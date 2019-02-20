import iso8601


class GeEvent:
    def __init__(self, event_id, summary, start, end):
        self.event_id = event_id
        self.summary = summary
        self.start = start
        self.end = end
        try:
            self.duration = iso8601.parse_date(self.end) - iso8601.parse_date(self.start)
        except TypeError as e:
            return e


class GeeProject:
    def __init__(self, project_id):
        self.project_id = project_id
        self.events = []

    def add_event(self, event):
        self.events = self.events.append(event)
