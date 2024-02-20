#  Local search (Hill climbing)


The "N-queens" is a toy problem where you place the queens on the chessboard so that no queen can capture another queen. This means that there cannot be two queens on any row, column ("file" in chess lingo) or diagonal.

This problem is solvable starting from a 4x4 board, with 4 queens. For a NxN chessboard, the number of queens is always N. This is an optimization problem where we do not know the goal state. We construct a state and try to improve it.

The solution method selected moves the queens up/down in their corresponding columns. You can track the movement based on the maps and following the debugger in python along with it.

## Results

The hill climbing algorithm solves only a few boards out of the 100000 random boards given. The sharp drop in success rate as the board size goes from 5x5 to 6x6 and beyond reflects the exponential growth in problem complexity. The N-queens problem goes from being relatively tractable to highly challenging as N increases.
```
Board size of: 4
Amount of times ran: 100000
Solved amount 9695/100000 -> 9.70%

Board size of: 5
Amount of times ran: 100000
Solved amount 8944/100000 -> 8.94%

Board size of: 6
Amount of times ran: 100000
Solved amount 361/100000 -> 0.36%

Board size of: 7
Amount of times ran: 100000
Solved amount 300/100000 -> 0.30%

Board size of: 8
Amount of times ran: 100000
Solved amount 38/100000 -> 0.04%
```


### How to execute
Only used library is random, which be included in the default python3 installation.

Clone the project into your folder and in the corresponding project folder executing
```
python3 search.py
```
should be enough to execute the program which runs the hill climbing algorithm for board sizes from 4 up to 8 and displays how many of those boards were successfully solved.


## Output of the code

search.py runs the hill climbing algorithm on a randomly generated starting board. The algorithm will not always solve the table. Execute the program multiple times to get a solution (comment out the loop for the statistics function if not needed). 
```
Q Q . . 
. . . Q 
. . . . 
. . Q . 
Initial position value 1
Final value 0
. Q . . 
. . . Q 
Q . . . 
. . Q . 
Solved!

Board size of: 4
Amount of times ran: 100000
Solved amount 9695/100000 -> 9.70%

Board size of: 5
Amount of times ran: 100000
Solved amount 8944/100000 -> 8.94%

Board size of: 6
Amount of times ran: 100000
Solved amount 361/100000 -> 0.36%

Board size of: 7
Amount of times ran: 100000
Solved amount 300/100000 -> 0.30%

Board size of: 8
Amount of times ran: 100000
Solved amount 38/100000 -> 0.04%
```

**This has only been tested on**\
OS: Manjaro 23.0.0 Uranos\
Kernel: x86_64 Linux 5.15.128-1-MANJARO