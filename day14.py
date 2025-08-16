#Display art
import random
from data import logo
from data import vs
from data import data
print(logo)
# format the account data into printable formate.
def formate_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
#Generate a random account from the game data
game_should_continue = True
while game_should_continue:
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {formate_data(account_a)}")
    print(vs)
    print(f"Against B: {formate_data(account_b)}")

    #Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #check if user is correct
    #-get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    #-use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")

    else:
        print(f"Sorry, that's wrong! Final score {score}")
        game_should_continue = False