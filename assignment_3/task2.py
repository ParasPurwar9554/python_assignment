"""
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
    o   Square root of the number
    o   Natural logarithm (log base e) of the number
    o   Sine of the number (in radians)
3.   Displays the calculated results.

"""

import math

def calculate_math_functions():
   try:
     user_input = float(input("Enter a number:"))
     if user_input > 0:
        print(f"Square root: {math.sqrt(user_input)}")
        print(f"Logarithm: {math.log(user_input)}")
        print(f"Sine: {math.sin(user_input)}")
     else:
        print("Enter a valid input!")   
   except:
      print("Something went wrong!")

calculate_math_functions()      
      
   