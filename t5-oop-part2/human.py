from mammal import Mammal

class Human(Mammal):
    def __init__(self):
        super().__init__(2)

    def speak(self):
        print('Human speaks...')