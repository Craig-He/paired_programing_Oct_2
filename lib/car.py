from lib.tire import *

class Car():
    def __init__(self):
        self.tires: dict[str,Tire] = {}

    def add_tire(self, postiton: str):
        if self.tires.get(postiton):
            raise(TireAlreadyExistsError)
        tire = Tire(postiton)
        self.tires[postiton] = tire

    def add_tire_reading(self, postiton: str, pressure: float, tread_depth: float, timestamp: datetime.datetime):
        if not self.tires.get(postiton):
            raise(TireNotFoundError)
        data = TireData(pressure, tread_depth, timestamp)
        self.tires[postiton].add_reading(data)

    def car_overview(self):
        output = ""
        for tire in self.tires.values():
            output += f"Tire '{tire.position}': pressure: {tire.current.pressure}, tread_depth: {tire.current.tread_depth}, timestamp: {tire.current.timestamp.strftime('%D %X')}\n"
        return output
