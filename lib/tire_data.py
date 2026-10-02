import datetime


class TireData:
    def __init__(
        self, pressure: float, tread_depth: float, timestamp: datetime.datetime
    ):
        self.pressure = pressure
        self.tread_depth = tread_depth
        self.timestamp = timestamp

    def format_data(self):
        return f"pressure: {self.pressure}, tread_depth: {self.tread_depth}, timestamp: {self.timestamp.strftime('%D %X')}"
