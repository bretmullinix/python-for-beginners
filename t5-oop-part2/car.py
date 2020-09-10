from battery import Battery
from engine import Engine

class Car:
    def __init__(self, battery: Battery, engine: Engine):
        self.battery = battery
        self.engine = engine

    def start (self):
        print('Car is trying to start: ')
        self.battery.start(self.engine)

    def stop(self):
        print('Car is trying to stop: ')
        self.engine.stop()