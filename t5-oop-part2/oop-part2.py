# Create a mammal and call it's walk method

from mammal import Mammal



mammal = Mammal()
mammal.walk()
mammal.speak()

print("")
# Create a human and call it's walk method
from human import Human
human = Human()
human.walk()
human.speak()

print('')
# Use Composition and create a simplistic car
from engine import Engine
from battery import Battery
from car import Car
an_engine = Engine()
a_battery = Battery()
a_car = Car (a_battery, an_engine)

a_car.start()
print('-----------------------------\n')
a_car.stop()
