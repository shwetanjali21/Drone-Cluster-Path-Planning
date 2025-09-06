import matplotlib.pyplot as plt
import random

# Start and end points
start = (0, 0)
end = (10, 10)

# Obstacle (for example, at (5,5))
obstacle = (5, 5)

# Function to generate random path for drones
def generate_path(start, end, steps=15):
    x, y = start
    path_x, path_y = [x], [y]
    for _ in range(steps - 2):
        x += random.choice([-1, 0, 1])
        y += random.choice([-1, 0, 1])
        x = max(0, min(10, x))
        y = max(0, min(10, y))
        path_x.append(x)
        path_y.append(y)
    path_x.append(end[0])
    path_y.append(end[1])
    return path_x, path_y

# Two masters, each controlling 5 drones
cluster_A = [generate_path(start, end) for _ in range(5)]
cluster_B = [generate_path(start, end) for _ in range(5)]

plt.figure(figsize=(6, 6))

# Plot drones from Cluster A
for i, (x, y) in enumerate(cluster_A, start=1):
    plt.plot(x, y, marker='o', label=f'Cluster A Drone {i}')

# Plot drones from Cluster B
for i, (x, y) in enumerate(cluster_B, start=1):
    plt.plot(x, y, marker='s', label=f'Cluster B Drone {i}')

# Plot start, end, and obstacle correctly
plt.scatter(start[0], start[1], c='green', s=150, marker='D', label='Start')
plt.scatter(end[0], end[1], c='black', s=150, marker='*', label='Target')
plt.scatter(obstacle[0], obstacle[1], c='red', s=200, marker='X', label='Obstacle')

plt.xlim(-1, 11)
plt.ylim(-1, 11)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Drone Clusters Path Planning")
plt.legend()
plt.grid(True)
plt.show()
