# Assignment 1: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.
simple_list = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", 3.14, True]
temp_list = []  
# 2D List (List of Lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing Elements
first_element = simple_list[0]  # Outputs 1
#print(first_element)
second_row_first_col = matrix[1][0]  # Outputs 4

#modifying
# Adding elements
#print("Before Apprend Operation: ", simple_list)
simple_list.append(6)  # Adds 6 to the end
#print("After Append operation: ", simple_list)
simple_list.insert(1, 6)  
#print("After Insert operation: ", simple_list)

# Removing elements
simple_list.remove(6)  # Removes the first occurrence of 6
print("After Remove operation: ", simple_list)
popped_element = simple_list.pop()  # Removes and returns the last element
#print("Popped element:", popped_element)
#print("After Pop operation: ", simple_list)

# List Methods
# Join lists
combined_list = simple_list + mixed_list
#print("Combined List: ", combined_list)

# Sort lists
simple_list.sort()  # Sorts the list in place
#print("Sorted List: ", simple_list)



#Assignment 2: Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.
simple_tuple = (1, 2, 3, 4, 5)
comp_tuple=(1.23,4.5)
mixed_tuple = (1, "Hello", 3.14, True)
temp_tuple = ()  # Empty tuple
# Accessing elements
first_tuple_element = simple_tuple[0]
#print(first_tuple_element)

tuple_dict = {simple_tuple: "My Tuple",comp_tuple :"My tuple"}
#print(tuple_dict)



#Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.

data=[('jeny','D'),('mim','B'),('mili','A+')]

data.sort(key=lambda x: x[1])
print(data)
