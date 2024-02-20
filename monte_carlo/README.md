# Monte Carlo Method in Search

Connect Four is a game where the players take turns to drop colored tokens into a frame. Whoever gets 4 tokens of the same color in a row, column or diagonal, wins. This is a program that uses the Monte Carlo method to play against a human. The AI plays as O and the human player is X. If you want the AI to start then set player_turn = False in the play_game() function.

## Code Description

The program shows the position and asks for the next move. It then makes it's own move and displays the position again. This cycle repeats until the game is over. After every player move, the results of the simulation's win precentage are displayed for every playable column.

To increase/lower the difficulty then lower the number of simulations (N) in the pure_mc() function.  

The default settings use numbers 0-6 to display and input the columns that the token can be dropped to.

## Results
Example end result of AI winning the game.
```
Column: 0: 76.0%
Column: 1: 83.0%
Column: 2: 100.0%
Column: 3: 86.0%
Column: 4: 81.0%
Column: 5: 82.0%
Column: 6: 82.5%
| | | | | | | |
| | | | | | | |
|O| | | | | | |
|X| | | | | | |
|X| | | | | | |
|X|X|O|O|O|O|X|
 0 1 2 3 4 5 6
O wins!
```

## How to execute
This should work with a default python3.9 installation.

Clone the project into your folder and in the corresponding project folder executing
```
python3 mc.py
```
should start the game.

**This has only been tested on**\
OS: Manjaro 23.0.0 Uranos\
Kernel: x86_64 Linux 5.15.128-1-MANJARO
