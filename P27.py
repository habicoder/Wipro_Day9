#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
 
# class Bus(Vehicle):
#     pass
 
# School_bus = Bus("School Volvo", 12, 50)
 
# # Python's built-in type()
# print(type(School_bus))


class Vehicle:

    def __init__(self, name, mileage, capacity):

        self.name = name

        self.mileage = mileage

        self.capacity = capacity
 
class Bus(Vehicle):

    pass
 
School_bus = Bus("School Volvo", 12, 50)
 
# Python's built-in isinstance() function

print(isinstance(School_bus, Vehicle))

print(isinstance(School_bus, Bus))


