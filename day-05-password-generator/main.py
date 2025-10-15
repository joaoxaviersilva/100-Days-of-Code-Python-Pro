import random

# Lists representing possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message to the user
print("Welcome to the PyPassword Generator!")

# Ask the user how many letters, symbols, and numbers they want in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create an empty list to hold the characters of the password
password_list = []

# Add random letters to the password list based on user input
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers to the password list
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list to randomize the order of characters
random.shuffle(password_list)

# Join all characters from the list into a single string
password = ""
for char in password_list:
    password += char

# Print the generated password to the user
print(f"Your password is: {password}")
