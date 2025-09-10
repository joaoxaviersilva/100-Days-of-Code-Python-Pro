# Print a welcome message to the user
print("Welcome to the tip calculator!\n")

# Ask the user for the total bill amount and convert it to a float
bill = float(input("What was the total bill? $"))

# Ask the user what percentage tip they would like to give and convert it to an integer
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

# Ask the user how many people will split the bill and convert it to an integer
people = int(input("How many people to split the bill? "))

# Convert the tip percentage to a decimal
tip_as_percent = tip / 100

# Calculate the total bill amount including the tip, rounded to 2 decimal places
total_bill = round(bill * tip_as_percent + bill, 2 )

# Calculate the amount each person should pay, rounded to 2 decimal places
bill_per_person = round(total_bill / people, 2)

# Print the amount each person should pay
print(f"Each person should pay: ${bill_per_person}")
