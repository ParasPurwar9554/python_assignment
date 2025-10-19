"""
Task 1:Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
    Addition
    Subtraction
    Multiplication
    Division
3.  Displays the results of each operation on the screen."""

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

sum = num1 + num2
sub = num1 - num2
multiply = num1 * num2
division = num1 / num2

print("Addition: ",sum)
print("Subtraction: ",sub)
print("Multiplication: ",multiply)
print("Division: ",division)