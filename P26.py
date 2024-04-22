#question
#Define a property that must have the same value for every class instance (object)- class
class Vehicle:
    # Class attribute
    color = "White"

    def _init_(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage