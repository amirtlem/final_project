import sys
import pandas as pd 
from game_helpers import get_game_parameters, roll_dice, tuple_out, fixed_dice, re_roll_dice, get_player_choice, play_turn, visualize_stats


# Intializing high score tracking 
high_score = 0

# Get game parameters from command line arguments or inputs 
target, max_re_rolls, player_count = get_game_parameters() 
# Defining the player names based on the number of players chosen at the beginning and whether or not they play with the computer 
# If there is only 1 player, the computer plays with the user
if player_count == 1:
    player_names = ["Player"]
    computer = True
else: 
    # If there is more than 1 player, they play with the other player(s), not the computer 
    player_names = [f"Player {i+1}" for i in range(player_count)]
    computer = False 

# Intializing player statistics using a dictionary 
player_stats = {name: {"score" : 0, "turns" : 0} for name in player_names}
player_stats_df = pd.DataFrame.from_dict(player_stats) 

# Intializes turn counter 
turn_counter = 0
# Game loop 
# While the max scores are less than the target score 
while max(player_stats[name]["score"] for name in player_names) < target:
    current_turn_player = player_names[turn_counter % player_count]  # Select player based on turn counter
    print(f"\n{current_turn_player}'s turn!")
    
    turn_score = play_turn(current_turn_player, computer=(computer and player_stats[current_turn_player]["turns"] % player_count == 1))
    
    # Update player statistics dictionary
    player_stats[current_turn_player]["score"] += turn_score
    player_stats[current_turn_player]["turns"] += 1
    print(f"{current_turn_player}'s total score: {player_stats[current_turn_player]['score']}")

    # Sychronizing the data frame with the player_stats dictionary so that the accurate scores appear after each round 
    player_stats_df = pd.DataFrame.from_dict(player_stats) 
    # Printing player stats 
    print("\nPlayer Stats: ")
    print(player_stats_df)
    
    # Increment turns and switch to the next player
    turn_counter += 1 


# Determine the winner 
max_score = -1
winner = None
for i in range(len(player_names)):
    player_name = player_names[i]
    player_score = player_stats[player_name]["score"]
    if player_score > max_score:
        max_score = player_score
        winner = player_name


print(f"\n{winner} wins with a score of {max_score}!")

# Track and display high scores
if max_score > high_score: 
    high_score = max_score
    print(f"New high score is: {high_score}")
else: 
    print(f"Highscore to beat: {high_score}")

visualize_stats(player_stats_df)

# Write the results of the game to a file
with open("game_results.txt", "w") as file:
    file.write(f"Target Score: {target}\n")
    file.write(f"Max re-rolls: {max_re_rolls}\n")
    file.write(f"\nFinal Scores:\n")
    for name, stats in player_stats.items():
        file.write(f"{name}: {stats['score']}\n")
    file.write(f"Winner: {winner} with {max_score} points!\n")


print("Game results written to game_results.txt")
