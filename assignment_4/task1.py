"""
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""
try:
    fileName = "sample.txt"
    fileHandler= open("assignment_4/"+fileName,"r")
    line1 = fileHandler.readline()
    line2 = fileHandler.readline()
    print(f"Reading File Content: \n Line: 1 {line1.strip("\n")} \n Line 2: {line2.strip("\n")}")
    fileHandler.close()
except FileNotFoundError:
    print(f"Error: The File '{fileName}' was not found.")   
