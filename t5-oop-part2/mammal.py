class Mammal:
    def __init__(self, number_of_legs_needed_to_walk = 4):
        self.__number_of_legs_needed_to_walk = number_of_legs_needed_to_walk

    def get_number_of_legs_needed_to_walk(self):
        return self.__number_of_legs_needed_to_walk

    def walk(self):
        class_name = self.__class__.__name__.lower()
        number_of_legs_needed_to_walk = self.get_number_of_legs_needed_to_walk()
        print('The ' + class_name + ' walks on ' + str(number_of_legs_needed_to_walk) + ' legs.')

    def speak(self):
        print('Mammal speaking....')