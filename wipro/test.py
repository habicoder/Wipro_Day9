# test.py
from calc import Calculation
from fact import factorial

# Creating objects
calc_obj = Calculation()
fact_obj = factorial()

# Calling methods
print("Sum:", calc_obj.addtwo(5, 3))
print("Product:", calc_obj.prod(5, 3))
print("Factorial of 5:", fact_obj.fact(5))
