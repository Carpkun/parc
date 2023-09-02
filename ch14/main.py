from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower, b_follower):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

score = 0
# Displat art
print(logo)
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:

    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format
    print(f"Compare A : {format_data(account_a)}.")
    print(vs)
    print(f"Against B : {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on theit guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")

# Score keeping


# Making account at position B become the next account at position A





