import datetime
import pytest
from lib.tire_data import TireData
from lib.tire import Tire, TireAlreadyExistsError
from lib.car import *


def test_for_TireData_object():
    data = TireData(24.1, 7.2, datetime.datetime(2026, 10, 2, 12, 30, 0))
    assert data.pressure == 24.1
    assert data.tread_depth == 7.2
    assert data.timestamp == datetime.datetime(2026, 10, 2, 12, 30, 0)


def test_for_adding_tire_data():
    tire = Tire("front-left")
    data = TireData(24.1, 7.2, datetime.datetime(2026, 10, 2, 12, 30, 0))
    tire.add_reading(data)
    assert tire.current == data
    assert tire.history == []
    assert tire.get_readings() == [data]


def test_for_add_two_readings():
    tire = Tire("front-left")
    data = TireData(24.1, 7.2, datetime.datetime(2026, 10, 2, 12, 30, 0))
    tire.add_reading(data)

    data2 = data2 = TireData(23.1, 7.1, datetime.datetime(2026, 10, 3, 12, 30, 0))
    tire.add_reading(data2)

    assert tire.current == data2
    assert tire.history == [data]
    assert tire.get_readings() == [data, data2]


def test_for_adding_a_tire_to_car():
    car = Car()
    car.add_tire("front-left")
    assert isinstance(car.tires["front-left"], Tire)


def test_for_adding_two_tires_to_car():
    car = Car()
    car.add_tire("front-left")
    car.add_tire("front-right")

    assert isinstance(car.tires["front-left"], Tire)
    assert isinstance(car.tires["front-right"], Tire)


def test_for_TireAlreadyExistsError():
    car = Car()
    car.add_tire("front-left")
    with pytest.raises(TireAlreadyExistsError):
        car.add_tire("front-left")


def test_for_car_overview():
    car = Car()
    car.add_tire("front-left")
    car.add_tire("front-right")
    car.add_tire_reading(
        "front-left", 24.1, 7.2, datetime.datetime(2026, 10, 2, 12, 30, 0)
    )
    car.add_tire_reading(
        "front-right", 23.3, 6, datetime.datetime(2026, 10, 2, 12, 30, 0)
    )
    assert (
        car.car_overview()
        == "Tire 'front-left': pressure: 24.1, tread_depth: 7.2, timestamp: 10/02/26 12:30:00\nTire 'front-right': pressure: 23.3, tread_depth: 6, timestamp: 10/02/26 12:30:00\n"
    )


def test_for_TireNotFoundError():
    car = Car()

    with pytest.raises(TireNotFoundError):
        car.tire_history("back-left")


def test_for_tire_history():
    car = Car()
    car.add_tire("front-left")
    car.add_tire_reading(
        "front-left", 24.1, 7.2, datetime.datetime(2026, 10, 2, 12, 30, 0)
    )
    car.add_tire_reading(
        "front-left", 23.3, 6, datetime.datetime(2026, 10, 20, 12, 30, 0)
    )
    assert (
        car.tire_history("front-left")
        == "pressure: 24.1, tread_depth: 7.2, timestamp: 10/02/26 12:30:00\npressure: 23.3, tread_depth: 6, timestamp: 10/20/26 12:30:00\n"
    )
