import heapq
import math

# Define the A* search algorithm
def a_star_search(maze, start, goal, heuristic):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current, maze, rows, cols):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(
                        open_set,
                        (f_score[neighbor], neighbor)
                    )

    return []


# Helper to get valid neighbors
def get_neighbors(node, maze, rows, cols):
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    neighbors = []

    for dr, dc in directions:
        r = node[0] + dr
        c = node[1] + dc

        if (
            0 <= r < rows
            and 0 <= c < cols
            and maze[r][c] == 0
        ):
            neighbors.append((r, c))

    return neighbors


# Heuristic functions
def manhattan_distance(node, goal):
    return (
        abs(node[0] - goal[0])
        + abs(node[1] - goal[1])
    )


def euclidean_distance(node, goal):
    return math.sqrt(
        (node[0] - goal[0]) ** 2
        + (node[1] - goal[1]) ** 2
    )


# Helper to reconstruct path
def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    return path[::-1]


# Test the implementation
maze = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

# Using Manhattan Distance
path_manhattan = a_star_search(
    maze,
    start,
    goal,
    manhattan_distance
)

print(
    "Path with Manhattan Distance:",
    path_manhattan
)

# Using Euclidean Distance
path_euclidean = a_star_search(
    maze,
    start,
    goal,
    euclidean_distance
)

print(
    "Path with Euclidean Distance:",
    path_euclidean
)
