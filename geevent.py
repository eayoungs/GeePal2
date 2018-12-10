class GeEvent:
    def __init__(self, summary, start, end):
        self.summary = summary
        self.start = start
        self.end = end

    def calc_duration(self, start, end):
        self.duration = self.end - self.start
