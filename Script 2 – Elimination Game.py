# For the elimination_round function I wanted it to take in a list of players
# and the number of players to eliminate
# Depending on how many users the player wants to eliminate it will choose a random number each time
# It will eliminate the player associated with the index
# When this is done then the clock function will run

# In the function countdown_clock it displays a countdown timer for number of seconds depending on the parameter
# It takes in a number and will print this number counting down until it reaches 0
# After printing each second it pauses for 1 second to simulate a ticking clock.

# I have listed my sources as I referenced them throughout my code.

import random
import time


def elimination_round(elimination_list, elimination_number):
    counter = 0
    # Previously I was doing this:
    # randomly eliminate between 2 – 6 players
    # no_of_eliminated_players = random.randint(2, 6)

    # Now the user chooses how many players are eliminated
    while counter < elimination_number:
        # Randomly generating the index of eliminated player
        # Doing this within loop so that it doesn't go out of bounds
        elimination_index = random.randint(0, len(player_list) - 1)  # Slide 33 - Source: Lecture 11

        # Finding the name of the player using their index.
        eliminated_player = elimination_list[elimination_index]  # Source: Slide 5 - Lecture 13

        print(f"{eliminated_player} has been eliminated.")
        # Source: Slide 27 - Lecture 13
        elimination_list.remove(eliminated_player)  # Removing them from list
        counter += 1

    return elimination_list


def countdown_clock(seconds):
    while seconds:
        # Source: Slide 14 - Lecture 12
        print(seconds, end=' ')  # printing current second, all on same line
        time.sleep(1)  # pausing for a second
        seconds -= 1  # taking a second of timer
    print("Next round!")


if __name__ == '__main__':
    player_list = []
    i = 0
    no_of_players = 12

    # Getting a name for each player
    while i < no_of_players:
        player = input(f"Enter name for player #{i+1}: ")  # asking the user for a value
        player_list.append(player)
        i += 1

    # Making a copy of the original player list
    original_player_list = player_list[:]

    while len(player_list) > 1:
        elimination_choice = int(input(f"Enter how many players you want to eliminate: "))
        # Checking that input is valid
        while elimination_choice > 6 or elimination_choice < 2:
            elimination_choice = int(input("Enter a number between 2-6: "))

        # Using send-forth message to update player list
        player_list = elimination_round(player_list, elimination_choice)
        # 30-second timer until next round
        countdown_clock(30)  # passing 30 seconds as a parameter into the timer

    print("\nResult tuple:", tuple(player_list))  # Converting list to tuple
    print("\nOriginal List:", original_player_list)
    print("\nGame over")
