#  Assignment 1: Write a Python script that determines if a number is positive, negative, or zero using if-elif-else.
number=112

if number > 0:
    print("The number is positive.")
elif number < 0:
   print("The number is negative.")
else:
    print("The number is zero.")
    
    
    


# Assignment 2: Create a script that checks if a person is eligible for a senior citizen discount based on age and residency.




min_age = 60
Residency ='USA'
age=int(input('Enter age:'))
residency=('Enter residency')

# Check eligibility for senior citizen discount
if age >= min_age and residency == 'Residency':
     print("Congratulations! You are eligible for a senior citizen discount.")
else:
     print("Sorry, you are not eligible for a senior citizen discount.")
    
    

# Assignment 3: Write a script that simulates a basic login system. Check username and password correctness.
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}


username = input("Enter your username: ")
password = input("Enter your password: ")

if username in user_credentials and user_credentials[username] == password:
    print("Login successful! Welcome, " + username + "!")
else:
    print("Invalid username or password. Please try again.")