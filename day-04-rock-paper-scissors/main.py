import random

# Define ASCII art for each hand gesture: Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store the ASCII drawings in a list for easy access by index
game_images = [rock, paper, scissors]

# Ask the player to choose between Rock (0), Paper (1), or Scissors (2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Show the player's chosen gesture if input is valid
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

# Randomly generate the computer’s choice between 0 and 2
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Evaluate game outcomes based on user and computer choices
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")  # Rock beats Scissors
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")  # Scissors lose to Rock
elif computer_choice > user_choice:
    print("You lose!")  # Higher number wins in standard conditions
elif user_choice > computer_choice:
    print("You win!")   # Lower number beats higher in exceptions
elif computer_choice == user_choice:
    print("It's a draw!")  # Same choice results in a tie
