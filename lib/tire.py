import datetime
from lib.tire_data import TireData


class Tire:
    def __init__(self, position: str):
        self.position = position
        self.current: TireData | None = None
        self.history: list[TireData] = []

    def add_reading(self, tire_data: TireData):
        # append current to history
        # set current to new data
        if self.current:
            self.history.append(self.current)
        self.current = tire_data

    def get_readings(self):
        # return current + history
        history = self.history
        history.append(self.current)

        return history
