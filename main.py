from art import logo, vs
from data import data
import random

print(logo)

def start_game():

    def shuffle_data():
    
        for i in range(len(data)):
            rand_index = random.randint(0, len(data) - 1)
            temp = data[rand_index]
            data[rand_index] = data[i]
            data[i] = temp

    shuffle_data()

        
    queue = []
    selected_person = data.pop()
    queue.append(selected_person)

    score = 0
    
    continue_game = True

    while continue_game:

        print(f"Compare A: {queue[-1]['name']}, a {queue[-1]['description']}, from {queue[-1]['country']}.")
        
        print(vs)

        print(f"Against B: {data[-1]['name']}, a {data[-1]['description']}, from {data[-1]['country']}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ")
        
        follower_count_A = queue[-1]['follower_count']
        follower_count_B = data[-1]['follower_count']
        
        if (follower_count_A > follower_count_B and guess == 'A') or (follower_count_A < follower_count_B and guess == 'B'):
            score += 1
            print(f"You're right! Current score: {score}")
            selected_person = data.pop()
            queue.append(selected_person)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False
            play_again = input("Would you like to play again? Type 'y' or 'n': ")
            if play_again == "y":
                start_game()
            else:
                break

start_game()