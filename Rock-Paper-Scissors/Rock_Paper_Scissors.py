import random

# Define choices and initialize score variables
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

# Game loop for 3 rounds
for i in range(3):
    # Take user input
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Validate user input
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

# Display final results
print("\nFinal Scores:")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("Computer won the game. Better luck next time!")
else:
    print("It's a tie overall!")
