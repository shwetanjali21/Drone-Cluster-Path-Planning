import matplotlib.pyplot as plt
import heapq
import random

# ----------------- A* Functions -----------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def astar(start, goal, grid, obstacles):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
        for dx, dy in neighbors:
            neighbor = (current[0]+dx, current[1]+dy)
            if (0 <= neighbor[0] < grid[0]) and (0 <= neighbor[1] < grid[1]):
                if neighbor in obstacles:
                    continue
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

# ----------------- Simulation Setup -----------------
grid_size = (20, 20)
start = (0, 0)
goal = (18, 18)

# Obstacles (wall-like)
obstacles = {(5, y) for y in range(3, 15)} | {(x, 10) for x in range(7, 18)}

# Generate small offsets for different drones
def jitter_goal(base_goal, max_offset=2):
    return (
        min(grid_size[0]-1, max(0, base_goal[0] + random.randint(-max_offset, max_offset))),
        min(grid_size[1]-1, max(0, base_goal[1] + random.randint(-max_offset, max_offset)))
    )

# Two clusters (each 5 drones)
cluster_A_goals = [jitter_goal(goal) for _ in range(5)]
cluster_B_goals = [jitter_goal(goal) for _ in range(5)]

cluster_A_paths = [astar(start, g, grid_size, obstacles) for g in cluster_A_goals]
cluster_B_paths = [astar(start, g, grid_size, obstacles) for g in cluster_B_goals]

# ----------------- Plotting -----------------
plt.figure(figsize=(7,7))

# Obstacles
for (ox, oy) in obstacles:
    plt.scatter(ox, oy, c="red", marker="X")

# Cluster A paths
for i, path in enumerate(cluster_A_paths, start=1):
    if path:
        xs, ys = zip(*path)
        plt.plot(xs, ys, marker="o", label=f"Cluster A Drone {i}")

# Cluster B paths
for i, path in enumerate(cluster_B_paths, start=1):
    if path:
        xs, ys = zip(*path)
        plt.plot(xs, ys, marker="s", label=f"Cluster B Drone {i}")

# Start & Goal
plt.scatter(start[0], start[1], c="green", marker="D", s=120, label="Start")
plt.scatter(goal[0], goal[1], c="black", marker="*", s=150, label="Main Goal")

plt.xlim(-1, grid_size[0])
plt.ylim(-1, grid_size[1])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.title("Multi-Drone Path Planning with A* (2 Clusters)")
plt.tight_layout()
plt.show()
