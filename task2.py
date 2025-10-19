"""
Task 2: Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like:
"""

fname = str(input("Enter your first name : "))
lname = str(input("Enter your last name : "))
fullName = fname +" "+ lname

print(f"Hello, {fullName}! Welcome to the Python Program.")