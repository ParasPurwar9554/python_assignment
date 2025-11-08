"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""
# Writing a file
fileName = "output.txt"
inputContent = input("Enter to write to the file:")
fileHandler = open("assignment_4/"+fileName,"w")
fileHandler.write(inputContent)
fileHandler.close()
print("Data successfully written to "+ fileName)
print()
# Appending a file
addinputContent = input("Enter additional text to append:")
fileHandlerAp = open("assignment_4/"+fileName,"a")
fileHandlerAp.write("\n"+addinputContent)
fileHandlerAp.close()
print("Data successfully appended.")
print()
# Reading a file

fileHandlerRead = open("assignment_4/"+fileName,"r")
content = fileHandlerRead.read()
print(f"Final content to {fileName} \n {content}")
fileHandlerRead.close()







