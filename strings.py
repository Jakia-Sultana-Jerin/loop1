simple_string = "Hello, Python learners!"
# print(simple_string[0])  # Accessing the first character

# String Methods
# Finding substrings
print(simple_string.find('Python')) 

# Assignment 1: Create a string that contains a simple bio data like name, age, and country. Extract each piece of information and print them separately.

data = "Name: John Doe, Age: 30, Country: USA"

# Split the  data string by commas
split_data = data.split(", ")

# Iterate through each piece of information and print them separately
for info in split_data:
    # Split each piece of information by the colon
    key, value = info.split(":")
    # Print the key and value separately
    #print(f"{key}: {value}")
    
    
# Assignment 2: Create a formatted string that includes data from a list or dictionary. For example, use a dictionary to store a person's information and format a string to include it.
person_info = {
    "name": "Jimi",
    "age": 30,
    "country": "USA"
}

# Format a string to include person's information
formatted_string = "Name: {name}, Age: {age}, Country: {country}".format(**person_info)

# Print the formatted string
#print(formatted_string)




#Assignment:3
def count_characters(input_string):
    # Initialize an empty dictionary to store character counts
    char_counts = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is already in the dictionary
        if char in char_counts:
            # If so, increment its count
            char_counts[char] += 1
        else:
            # If not, add it to the dictionary with a count of 1
            char_counts[char] = 1
    
    # Return the dictionary with character counts
    return char_counts

# Test the function
input_string = "hello"
result = count_characters(input_string)
#print(result)



import re
text_with_hashtags = "This is a #great day to learn #regex in #Python!"
hashtags = re.findall(r"#(\w+)", text_with_hashtags)
print("Hashtags:", hashtags)