from lib.tire import *


class Car:
    def __init__(self):
        self.tires: dict[str, Tire] = {}

    def add_tire(self, position: str):
        if self.tires.get(position):
            raise (TireAlreadyExistsError)
        tire = Tire(position)
        self.tires[position] = tire

    def add_tire_reading(
        self,
        position: str,
        pressure: float,
        tread_depth: float,
        timestamp: datetime.datetime,
    ):
        if not self.tires.get(position):
            raise (TireNotFoundError)
        data = TireData(pressure, tread_depth, timestamp)
        self.tires[position].add_reading(data)

    def car_overview(self):
        output = ""
        for tire in self.tires.values():
            output += f"Tire '{tire.position}': {tire.current.format_data()}\n"
        return output

    def tire_history(self, position: str):
        if not self.tires.get(position):
            raise (TireNotFoundError)

        output = ""
        history = self.tires[position].get_readings()
        for data in history:
            output += f"{data.format_data()}\n"

        return output
