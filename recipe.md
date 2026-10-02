As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were


```python
class Car:
    def __init__(self):
        self.tires = {"front-left": Tire, "front-right": Tire, ...}


    def add_tire(self, position):
        # check if tire in same position, throw error
        # add new tire under position


    def car_overview(self):
        # print current and history for each tire
        # positions, current readings and timestamps

    def tire_history(self, position):
        # print the reading history for that tire
        # throw error if position doesn't exist
    
    def add_tire_reading(self, position, pressure, tread_depth, timestamp)
        #call the add tire reading to the relevant tire object indicated by the position parameter
        # tire data is are passed into the add_reading method

    


class Tire:
    def __init__(self, position):
        self.position = "front-left" etc
        self.current = TireData
        self.history = [TireData, TireData]

    def add_reading(self, pressure, tread_depth, timestamp):
        # append current to history
        # set current to new data

    def get_readings(self):
        # return current + history


class TireData:
    def __init__(self, pressure, tread_depth, timestamp):
        self.pressue # float
        self.tread_depth # float
        self.timestamp # datetime


```

## Tests

### TireData
```python
data = TireData(24.1, 7.2, datetime.datetime(2026, 10, 2, 12, 30, 0))
data.pressure => 24.1
data.tread_depth => 7.2
data.timestamp => datetime.datetime(2026, 10, 2, 12, 30, 0)
```


### Tire
```python
tire = Tire("front-left")
data = TireData(24.1, 7.2, datetime.datetime(2026, 10, 2, 12, 30, 0))
tire.add_reading(data)

tire.current => data
tire.history => []
tire.get_readings() => [data]

data2 = TireData(23.1, 7.1, datetime.datetime(2026, 10, 3, 12, 30, 0))
tire.add_reading(data2)

tire.current => data2
tire.history => [data]
tire.get_readings() => [data, data2]
```

### Car
```python
car = Car()
car.add_tire("front-left")
isinstance(car.tires["front-left"], Tire) => True
car.tires["front-left"].position => "front-left"

car.add_tire("front-right")
isinstance(car.tires["front-right"], Tire) => True
car.tires["front-right"].position => "front-right"

car.add_tire("front-left") => raises TireAlreadyExistsError

car.car_overview() => "Tire 'front-left': pressure: x, tread_depth: x, timestamp: x"

car.tire_history('front-left') => # output list of readings
car.tire_history("back-left") => raises TireNotFoundError


```