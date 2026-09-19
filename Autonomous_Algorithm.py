# Install the PySAT package
!pip -q install python-sat

# Importing required libraries
from pysat.solvers import Glucose3


# Step 1: Define the grid size and initialize the environment
GRID_SIZE = 4  # 4x4 grid

# Define the knowledge base as a list of facts
knowledge_base = []

# Add known facts
knowledge_base.append(("Breeze", 1, 2))
knowledge_base.append(("Stench", 2, 1))


# Step 2: Define rules for inference
# If there is a Breeze, there is a Pit in an adjacent cell
def add_breeze_rule(kb, x, y):
    adjacent_cells = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]

    for cell in adjacent_cells:
        if (
            1 <= cell[0] <= GRID_SIZE
            and 1 <= cell[1] <= GRID_SIZE
        ):
            kb.append(("Pit", cell[0], cell[1]))


# Add rules to the knowledge base
add_breeze_rule(knowledge_base, 1, 2)


# Create integer SAT variables for propositions
proposition_ids = {}


def get_proposition_id(proposition):
    if proposition not in proposition_ids:
        proposition_ids[proposition] = len(proposition_ids) + 1

    return proposition_ids[proposition]


# Step 3: Implement the propositional logic inference mechanism
def infer(knowledge_base, query):
    solver = Glucose3()

    # Encode every known fact as a positive SAT clause
    for fact in knowledge_base:
        fact_id = get_proposition_id(fact)
        solver.add_clause([fact_id])

    # Determine whether the requested location is safe
    if query[0] == "Safe":
        position = (query[1], query[2])
        pit_proposition = ("Pit", position[0], position[1])

        pit_id = get_proposition_id(pit_proposition)

        # Test whether the knowledge base entails a Pit here.
        # If KB + NOT Pit is unsatisfiable, Pit is known to be present.
        pit_is_known = not solver.solve(
            assumptions=[-pit_id]
        )

        return not pit_is_known

    # General proposition query
    query_id = get_proposition_id(query)

    # If KB + NOT query is unsatisfiable,
    # then the query is entailed by the knowledge base.
    query_is_entailed = not solver.solve(
        assumptions=[-query_id]
    )

    return query_is_entailed


# Step 4: Test the agent in the Wumpus World environment
def test_agent():
    # Initial position
    position = (1, 1)

    while True:
        print(f"Agent at {position}")

        # Check for safety
        if infer(
            knowledge_base,
            ("Safe", *position)
        ):
            print(f"{position} is safe.")
        else:
            print(f"{position} is not safe.")

        break


# Run the test
test_agent()
