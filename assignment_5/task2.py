"""
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

"""
try:
    myList = list(range(1, 11))
    extractList = myList[:5]
    reverseList = extractList[::-1]
    print("Original list: ",myList)
    print("Extracted first five elements: ",extractList)
    print("Reversed extracted elements: ",reverseList)
except Exception as e:
    print("An unexpected error occurred:", e)    
