# Q-learning algorithm and the Gym library

See https://gymnasium.farama.org/environments/toy_text/taxi/ for an animated map.

The episode starts with the passenger at the (R)ed, (G)reen, (B)lue or (Y)ellow square. The passenger wants to go to one of the other squares R, G, B, Y. The taxi is at a random location.

At each time step we receive the state, which is an integer:

((taxi_row * 5 + taxi_col) * 5 + passenger_location) * 4 + destination

See the official documentation for the possible values. An integer representing the full state is already very convenient for Q-learning, so you don't actually have to decode the state in your program.

Possible actions:

    0,1,2,3 - movement down, up, right, left
    4 pick up passenger
    5 drop off passenger

The "pick up" and "drop off" actions are always available but if there is no passenger or the drop off location is not where the passenger wanted to go, the taxi receives a penalty. Other conditions:

    Each step the taxi recieves a reward of -1
    If the taxi performs an invalid pick up or drop off action, the reward is -10
    If the taxi drops off the customer at the destination, the reward is +20. The episode ends

We let each episode run for 200 steps at most.

## Results
Check episode_scores_with_average.png image for results at 0.5 learning rate.

## How to run the program
This should work with a default python3.9 installation.

Clone the project into your folder and in the corresponding project folder execute
```
python3 taxi.py
```

**This has only been tested on**\
OS: Manjaro 23.0.0 Uranos\
Kernel: x86_64 Linux 5.15.128-1-MANJARO
