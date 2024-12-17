# importing the random module 
import random 
# importing the sys module 
import sys 
# importing the pandas module 
import pandas as pd
# importing the seaborn module  
import seaborn as sns
# importing the matplotlib module 
import matplotlib.pyplot as plt 
# importing the time module 
import time  

def get_game_parameters():
    """
    Retrieves game parameters from command-line arguments or prompts the user for input.
    Returns:
        tuple: (target score, maximum re-rolls, number of players).
    """
    try:
        if len(sys.argv) > 1:
            target = int(sys.argv[1])
        else:
            target = int(input("Enter the target score to win or default to 50: ") or 50)

        if len(sys.argv) > 2:
            max_re_rolls = int(sys.argv[2])
        else:
            max_re_rolls = int(input("Enter the maximum re-rolls or default to 5: ") or 5)

        if len(sys.argv) > 3:
            player_count = int(sys.argv[3])
        else:
            player_count = int(input("Enter the number of players (1-4) or default to 2: ") or 2)

        player_count = max(1, min(player_count, 4))
    except ValueError:
        print("Invalid input. Using default values.")
        return 50, 5, 2  

    return target, max_re_rolls, player_count


def roll_dice():
    """ Simulates rolling 3 dice. """
    return [random.randint(1, 6) for _ in range(3)]


def tuple_out(dice):
    """ Checks if all three dice are the same, indicating the player has 'tupled out'. """
    return dice[0] == dice[1] == dice[2]


def fixed_dice(dice):
    """ Identifies indices of dice that should be fixed if two dice are the same. """
    counts = {x: dice.count(x) for x in dice}
    fixed_indices = []
    # Defines what a fixed dice is 
    for i in range(len(dice)):
        if counts[dice[i]] == 2:
            fixed_indices.append(i)
    return fixed_indices


def re_roll_dice(dice, fixed_indices):
    """ Re-rolls only non-fixed dice """
    # Uses the fixed_indices from the fixed_dice function to identify what a fixed dice it 
    return[random.randint(1,6) if i not in fixed_indices else dice[i] for i in range(3)]

def get_player_choice(player_name):
    """ Validates the input for stopping or continuing the turn."""
    # Gives the user a chance to input "y" or "n" if the input is not valid the first time
    while True:
        # Makes sure that the user only uses "y" and "n" when asked if they want to continue
        #.strip() and .lower() make it so that white space and upper case doesn't matter
        choice = input(f"{player_name}, stop and keep score? (y/n): ").strip().lower()
        if choice == "y":
            return choice 
        elif choice == "n":
            return choice 
        else: 
            # Error message if input is invalid 
            print("Invalid input. Please enter 'y' or 'n'.")

def play_turn(player_name, max_re_rolls, computer=False):
    """ Plays one turn for a player."""
    # Records the start time 
    start_time = time.time()


    dice = roll_dice()
    roll_history = [tuple(dice)]
    print(f"{player_name} rolls: {dice}")
    
    # Check if the player tupled out
    if tuple_out(dice):
        print(f"Tuple out! {player_name} scores 0 points this turn.")
        return 0

    # Check if the player rolled a fixed dice 
    fixed = fixed_dice(dice)
    if fixed:
        print(f"{player_name} rolled a fixed dice! The score will be kept.")
        score = sum(dice)
        print(f"{player_name} scores {score} points this turn.")
        print(f"Roll history for this turn: {roll_history}")
        return score

    re_roll_count = 0  # Initialize re-roll count

    while re_roll_count < max_re_rolls:  
        # Limit the number of rerolls
        if computer:
            stop = "y" if sum(dice) >= 12 or random.choice([True, False]) else "n"
        else:
            stop = get_player_choice(player_name)

        # If the player decides to stop the game 
        if stop == "y":
            score = sum(dice)
            print(f"{player_name} scores {score} points this turn.")
            print(f"Roll history for this turn: {roll_history}")
            # Ends the time 
            end_time = time.time()
            print(f"Turn Duration: {end_time-start_time:.2f} seconds")
            return score

        # If the player decides to re-roll
        re_roll_count += 1
        # Re-roll only non-fixed dice 
        dice = re_roll_dice(dice, fixed) 
        roll_history.append(tuple(dice))
        print(f"{player_name} re-rolls: {dice}")

        # Check for tuple out after re-roll
        if tuple_out(dice):
            print(f"Tuple out! {player_name} scores 0 points this turn.")
            # Ends the time 
            end_time = time.time()
            print(f"Turn Duration: {end_time-start_time:.2f} seconds")
            return 0

        # Recalculate fixed dice after each re-roll
        fixed = fixed_dice(dice) 
        if fixed:
            print(f"{player_name} rolled fixed dice: {dice}. Turn ends.")
            score = sum(dice)
            print(f"{player_name} scores {score} points this turn.")
            print(f"Roll history for this turn: {roll_history}")
            # Ends the time 
            end_time = time.time()
            print(f"Turn Duration: {end_time-start_time:.2f} seconds")
            return score

def visualize_stats(player_stats_df,player_stats):
    """ Visualizes the player statistics in bar plot form using seaborn and matplotlib module"""

    # Making player_stats into a list of dictionaries to make it easier to plot 
    data = []
    for player, stats in player_stats.items():
        data.append({
            'Player': player,
            'Score': stats['score'],
            'Turns': stats['turns']
        })

    # Converting the list of dictionaries to a data frame 
    player_stats_df = pd.DataFrame(data)
    # plotting the scores of each player 
    sns.barplot(x = player_stats_df.index, y = 'Score', data = player_stats_df)
    plt.title('Player Scores')
    plt.xlabel('Player')
    plt.ylabel('Score')
    plt.show()

    # plotting the number of turns taken by each player 
    sns.barplot(x = player_stats_df.index, y = 'Turns', data = player_stats_df)
    plt.title('Player Turns')
    plt.xlabel('Player')
    plt.ylabel('Number of turns')
    plt.show()