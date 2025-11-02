"""
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

"""

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
num = int(input("Enter a number: "))    
if num > 0:
    result = factorial(num)
    print(f"Factorial of {num} is : {result}")
else:
    print("Please enter a positive integer.")    


    
    