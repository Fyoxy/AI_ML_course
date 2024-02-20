#  Path finding on a 2D map

The problem is to find a path on the map from a given start point to end point. The project has these parts:

- breadth first search on a small map (bfs.py)
- search on a larger map (ai.py)
- heuristic search (ai.py)

This project uses multiple algorithms, such as: breadth first search, greedy search, and A* search. The goal is to experiment and see how efficient they are in finding the solution and if they can find an optimal solution.

## Output of the code

bfs.py is the first solution to using the breath first search on a small given map. It will output a marked path 

ai.py is the main file of this program which will run all of the algorithms and print out a table as shown below.
```
-----------+-------------+------+------------+----------
| Algorithm | Map         | Cost | Iterations | Time (s) |
-----------+-------------+------+------------+----------
| BFS       | cave300x300 | 554  | 47233      | 0.29187  |
| BFS       | cave600x600 | 1247 | 197804     | 0.94091  |
| BFS       | cave900x900 | 1843 | 450414     | 2.18958  |
-----------+-------------+------+------------+----------

-----------+-------------+------+------------+----------
| Algorithm | Map         | Cost | Iterations | Time (s) |
-----------+-------------+------+------------+----------
| greedy    | cave300x300 | 982  | 3358       | 0.02114  |
| greedy    | cave600x600 | 1973 | 6293       | 0.04511  |
| greedy    | cave900x900 | 4129 | 29496      | 0.18583  |
-----------+-------------+------+------------+----------

-----------+-------------+------+------------+----------
| Algorithm | Map         | Cost | Iterations | Time (s) |
-----------+-------------+------+------------+----------
| A*        | cave300x300 | 554  | 8202       | 0.05510  |
| A*        | cave600x600 | 1247 | 60472      | 0.44602  |
| A*        | cave900x900 | 1843 | 93999      | 0.77652  |
-----------+-------------+------+------------+----------
```

The ai.py program will also generate marked map files into the results folder for every algorithm and corresponding map. The route taken by algorithm will be shown as ".".

## Results

Both the BFS and A* algorithms are able to find the most cost efficient solutions to the mazes. Just with the input of knowing where the goal is the A* algorithm is a lot faster than the BFS method.

Greedy search outperforms both of the other algortihms by time, but lacks the cost efficiency. Then again the total number of iterations is far less than the other methods.

Your results may vary when executing this code, but the optimal path solutions should be the same:\
300x300 554\
600x600 1247\
900x900 1843

### How to execute
Only used libraries are: Queue, PriorityQueue, and time, which should all be included in the default python3 installation.

Clone the project into your folder and in the corresponding project folder executing
```
python3 ai.py
```
should be enough to execute the main program which tests all the algorithms mentioned before.

**This has only been tested on**\
OS: Manjaro 23.0.0 Uranos\
Kernel: x86_64 Linux 5.15.128-1-MANJARO
