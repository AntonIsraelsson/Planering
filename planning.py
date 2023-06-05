# A planning system based on OR-Tools
from ortools.sat.python import cp_model

# Create the model.
model = cp_model.CpModel()

# Set up the employees