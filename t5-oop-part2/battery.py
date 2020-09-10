from engine import Engine


class Battery:
    def __init__(self):
        pass

    def start (self, engine: Engine):
        print('\tBattery sending engine electric signal to start')
        engine.start()