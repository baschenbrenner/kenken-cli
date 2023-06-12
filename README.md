# kenken-cli
A CLI application that allows the user to play a 4x4 game of Kenken.

In this CLI there will be users, games, and groupings

A game will consist of a 4x4 grid
A game wil have many groupings. For a grouping to be sensible, the cells will have to be adjacent to each other. 

A user will be able to sign in and access previous results and play a new game or pick up on a saved game.

Python app for kenken 4x4 puzzle
1. Randomly build a 4x4 structure [x]
2. Randomly create groupings of 2's and 3's with remainders filled in [x]
3. Figure out how to show board [x]
4. Figure out how to show the rule (3x, 2/, etc.) in the top left box based on the random groupings [x]
5. Program suite of input tools that allows a person to enter a digit into a box, edit, or remove a digit [x]
6. Program a has won function that evaluates the win and gives the option to reset and start again. [x]
7. Figure out a way to track stats for a user, including games attempted, games won, and (stretch) time for each win [x]
8. Add note taking feature for person to write notes to themselves about games they played [x]

Expected flow for CLI:
1) welcome message, prompt for name
2) if name already exists ask if they want to continue as that user (by providing special word)
3) if name doesn't exist, create a new user and print explanations

from 2)
 if yes, print list of options
 if no, exit from game

list of options
play new game, 
look at previous games
exit

Next steps - debugging - what unexpected inputs cause the game to crash?


