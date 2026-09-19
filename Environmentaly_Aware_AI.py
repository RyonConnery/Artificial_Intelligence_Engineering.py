# Step 1: Import necessary libraries
from collections import defaultdict, deque


# Step 2: Define the environment as a graph
class Environment:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_connection(self, room1, room2):
        self.graph[room1].append(room2)
        self.graph[room2].append(room1)


# Step 3: Build the planning graph
environment = Environment()

environment.add_connection("A", "B")
environment.add_connection("B", "C")
environment.add_connection("C", "D")


# Step 4: Implement the planning graph algorithm
def planning_graph(initial_state, goal_state, graph):
    # Initialize the planning graph
    plan_graph = []

    queue = deque([
        (initial_state, [])
    ])

    visited = set()

    while queue:
        current, actions = queue.popleft()

        # If the goal is reached, return the sequence of actions
        if current == goal_state:
            return actions

        # Mark the room as visited
        visited.add(current)

        # Explore adjacent rooms
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(
                    (
                        neighbor,
                        actions + [
                            f"Move({current}, {neighbor})"
                        ]
                    )
                )

                plan_graph.append(
                    (current, neighbor)
                )

    return None  # No plan found


# Step 5: Test the planning agent
initial_state = "A"
goal_state = "D"

plan = planning_graph(
    initial_state,
    goal_state,
    environment.graph
)


# Display the results
if plan:
    print("Plan found:")

    for step in plan:
        print(step)

else:
    print("No plan found.")
