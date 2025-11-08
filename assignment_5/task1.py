"""
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

"""
try:
    students = {"Paras": 85,"Rahul": 90, "Priyanka": 78,"Amit": 92,"Saksham":"99"}

    stuName = input("Enter a student's name:").strip()
    if not stuName:
        raise ValueError("Student name cannot be empty.")
    
    stuMarks = students.get(f"{stuName}")
    if stuMarks != None:
        print(f"{stuName} marks: {stuMarks}")
    else:
        print("Student not found")
        
except ValueError as ve:
    print("Input Error:", ve)        
except Exception as e:
     print("An unexpected error occurred:", e)        
        


