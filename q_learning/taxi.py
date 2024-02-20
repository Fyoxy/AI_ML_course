import gym
import numpy as np
import matplotlib.pyplot as plt

# Create the Taxi environment
env = gym.make("Taxi-v3")

# Q-learning parameters
alpha = 0.5  # Learning rate
gamma = 0.6  # Discount factor
epsilon = 1.0  # Exploration-exploitation trade-off
min_epsilon = 0.01  # Minimum epsilon value
epsilon_decay = 0.99  # Epsilon decay rate

# Initialize Q-table with zeros
num_states = env.observation_space.n
num_actions = env.action_space.n
q_table = np.zeros((num_states, num_actions))

# Training parameters
num_episodes = 1000
episode_scores = []

# Q-learning training loop
for ep_num in range(num_episodes):
    observation, info = env.reset()
    ep_score = 0

    for t in range(200):
        # Epsilon-greedy policy
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(q_table[observation, :])  # Exploit

        # Take the selected action
        next_observation, reward, terminated, _, _ = env.step(action)

        # Update Q-table using the Q-learning update rule
        best_next_action = np.argmax(q_table[next_observation, :])
        q_table[observation, action] += alpha * (reward + gamma * q_table[next_observation, best_next_action] - q_table[observation, action])

        ep_score += reward
        observation = next_observation

        if terminated:
            # Passenger dropped off
            break

    # Decay epsilon
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

    # Append episode score to the list for tracking progress
    episode_scores.append(ep_score)

    print("Episode", ep_num, "score", ep_score)

env.close()

# Calculate moving average
window_size = 10
moving_average = np.convolve(episode_scores, np.ones(window_size)/window_size, mode='valid')

# Plot the learning progress with average line
plt.plot(episode_scores, label='Episode Score')
plt.plot(np.arange(window_size-1, len(episode_scores)), moving_average, label=f'Moving Average (window size={window_size})', linestyle='--', color='orange')
plt.xlabel('Episode')
plt.ylabel('Score')
plt.title('Q-learning Progress with Moving Average')
plt.legend()
plt.savefig('episode_scores_with_average.png')  # Save the plot as an image
plt.show()
