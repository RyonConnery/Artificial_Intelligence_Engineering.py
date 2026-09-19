# Install the required library
!pip -q install pgmpy

# Import required libraries
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD


# Step 1: Define the structure of the Bayesian network
# Nodes: Fever, Cough, Fatigue, Disease
model = DiscreteBayesianNetwork([
    ("Disease", "Fever"),
    ("Disease", "Cough"),
    ("Disease", "Fatigue")
])


# Step 2: Define the Conditional Probability Distributions (CPDs)

# CPD for Disease (prior probabilities)
cpd_disease = TabularCPD(
    variable="Disease",
    variable_card=3,
    values=[
        [0.1],  # Flu
        [0.3],  # COVID-19
        [0.6]   # None
    ],
    state_names={
        "Disease": [
            "Flu",
            "COVID-19",
            "None"
        ]
    }
)


# CPD for Fever given Disease
cpd_fever = TabularCPD(
    variable="Fever",
    variable_card=2,
    values=[
        [0.8, 0.9, 0.1],  # Fever = 1
        [0.2, 0.1, 0.9]   # Fever = 0
    ],
    evidence=["Disease"],
    evidence_card=[3],
    state_names={
        "Fever": [1, 0],
        "Disease": [
            "Flu",
            "COVID-19",
            "None"
        ]
    }
)


# CPD for Cough given Disease
cpd_cough = TabularCPD(
    variable="Cough",
    variable_card=2,
    values=[
        [0.7, 0.8, 0.2],  # Cough = 1
        [0.3, 0.2, 0.8]   # Cough = 0
    ],
    evidence=["Disease"],
    evidence_card=[3],
    state_names={
        "Cough": [1, 0],
        "Disease": [
            "Flu",
            "COVID-19",
            "None"
        ]
    }
)


# CPD for Fatigue given Disease
cpd_fatigue = TabularCPD(
    variable="Fatigue",
    variable_card=2,
    values=[
        [0.6, 0.85, 0.1],  # Fatigue = 1
        [0.4, 0.15, 0.9]   # Fatigue = 0
    ],
    evidence=["Disease"],
    evidence_card=[3],
    state_names={
        "Fatigue": [1, 0],
        "Disease": [
            "Flu",
            "COVID-19",
            "None"
        ]
    }
)


# Step 3: Add the CPDs to the model
model.add_cpds(
    cpd_disease,
    cpd_fever,
    cpd_cough,
    cpd_fatigue
)


# Step 4: Verify the model
assert model.check_model(), "Model validation failed!"


# Step 5: Perform inference using the model
inference = VariableElimination(model)

# Calculate disease probabilities given Fever=True and Cough=True
result = inference.query(
    variables=["Disease"],
    evidence={
        "Fever": 1,
        "Cough": 1
    }
)

print(result)
