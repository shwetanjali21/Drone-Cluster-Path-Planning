import matplotlib.pyplot as plt
import heapq

# A* helper functions
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
            return path[::-1]  # Reverse

        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]  # 4 directions
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

# Grid setup
grid_size = (20, 20)
start = (0, 0)
goal = (18, 18)

# Example obstacles
obstacles = {(5, y) for y in range(3, 15)} | {(x, 10) for x in range(7, 18)}

# Run A*
path = astar(start, goal, grid_size, obstacles)

# Plot
plt.figure(figsize=(6,6))
# Plot obstacles
for (ox, oy) in obstacles:
    plt.scatter(ox, oy, c="red", marker="X")
# Plot path
if path:
    xs, ys = zip(*path)
    plt.plot(xs, ys, c="blue", marker="o", label="Path")
# Start & Goal
plt.scatter(start[0], start[1], c="green", marker="D", s=100, label="Start")
plt.scatter(goal[0], goal[1], c="black", marker="*", s=120, label="Goal")
plt.legend()
plt.grid(True)
plt.title("A* Path Planning")
plt.show()
