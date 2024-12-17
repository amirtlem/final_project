Objective of the Tuple Out Dice Game: 
Players ranging from 1 player to 4 players play a dice game where the object of the game is to score the target points first. 
 
Game Rules: 
On each turn, a player rolls three dice. The values of the dice vary from 1 to 6. 
Tuple Out: If a player rolls three of the same number (e.g. 3,3,3) they have "tupled out" and they score zero points for that turn.
Fixed Dice: If a player rolls two dice with the same number (e.g. 4,4,5), those dice are "fixed" and they cannot re-roll. 
Re-rolling: Players can choose to re-roll as many times as they want (as long as there are no fixed dice/"tupled out") or they can stick to the default of 5 re-rolls. 
Ending the Turn: Players can end their turn any time by choosing to stop and keep their current score, which is the sum of the three dice however, if the player "tupled out" their turn ends immediately. 
Scores: The scores for each turn are the sum of the value of the 3 dice that were rolled 
Winning: The game will continue for a set amount of turns and the player with the highest score or the score closest to the pre-determined target score wins the game.

How a user can run the code: 
Start by running it in the Python terminal. The game will then ask the user what their target score is. 
They can choose any number they want or skip it and let it default to 50. After that, the game will ask the user how many turns they would like to be limited to. 
They can choose any number they want or skip it and let it default to 5. The game will then ask how many players are playing. 
The game will suggest 1-4, but the player can skip the question and it will default to 2 players. 
If the player puts in a wrong value (something that is not a number), an error message will pop up and the game will use the default values. 
The game will then output three numbers for player 1 and that user has the yes or no ("y" or "n") option whether to keep the numbers or re-roll for a better chance. 
If the player makes a typo when being asked if they want to continue or not, they will be prompted to answer the question again, allowing them to correct their mistake. 
Then once they are satisfied with their three dice outputs they can answer no to the re-roll question and it moves on to player 2 and they repeat the same steps as player 1 did. 
Both players can re-roll as many times as they want till they "tuple out", roll a "fixed" dice, or are happy with the sum of their dice points. 
Once a player decides to finish their turn, their score, roll history, turn duration, and a table summarizing all the player's points and turns they have taken so far will pop up. 
Then both players continue playing the game till one of the players reaches the target points. The player that reaches the target points first wins and the highest score reached during the game is tracked and reported after each game. 
The game's results are then saved to a txt file called game_results.txt, and two bar graphs will appear showing the number of turns each player took and the scores they ended with. 
