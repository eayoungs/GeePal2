class GeEvent:
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.start = end

    def get_duration(self, start, end):
        self.duration = self.end - self.start
