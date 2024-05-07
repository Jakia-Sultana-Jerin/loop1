simple_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(simple_dict['name'])  # Accessing value by key
print(simple_dict.get('address', "Dhaka"))  # Accessing value by key

# Updating dictionary
simple_dict['age'] = 31  # Updates the age
simple_dict['country'] = 'USA'  # Adds a new key-value pair
# print("Updated Dictionary: ", simple_dict)
removed_value = simple_dict.pop('country')  # Removes 'country' key and returns its value
print("Removed Value:", removed_value)
print("Dictionary after pop(): ", simple_dict)

# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.

data={'name':'jony','roll_number':12,'grades':'A'}
#print(data)
#print(data.get('age',20))

remove_data=data.pop('grades')
#print(remove_data)

#update
data.update({'name':'jimi','roll_number':14,'grades':'C'})
print (data)