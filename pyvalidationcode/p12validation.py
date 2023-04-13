import math
import matplotlib.pyplot as plt
import pandas as pd

# Problem Eqn
def view_factor(r1, r2, l, a):
    L = l/a
    R1 = r1/a
    R2 = r2/a
    R12 = R1 * R1
    R22 = R2 * R2
    x1 = (4 * (R1 * R1) * (L * L)) 
    x11 = x1 + math.pow((1- R12),2)
    x2 = (4 * (R2 * R2) * (L * L)) 
    x21 = x2 + math.pow((1- R22),2)
    X1 = math.pow(x11 ,0.5)
    X2 = math.pow(x21 ,0.5)
    vf = (1/4 * L)* (X2 - X1 + math.pow(R2,2) - math.pow(R1,2))
    return vf

# Define input configurations
configs = {
    "config1": {"r1": 1, "r2": 2, "l": 3, "a": 4},
    "config2": {"r1": 2, "r2": 3, "l": 4, "a": 5},
    "config3": {"r1": 3, "r2": 4, "l": 5, "a": 6},
    # add more configurations here...
}

# Calculate view factors for each configuration
vf_library = {}
for config_name, config in configs.items():
    r1 = config["r1"]
    r2 = config["r2"]
    l = config["l"]
    a = config["a"]
    vf = view_factor(r1, r2, l, a)
    vf_library[config_name] = vf

# Print library
print(vf_library)

# Save library into txt file
with open("12_vf_validation.txt", "w") as f:
    for config_name, config in configs.items():
        r1 = config["r1"]
        r2 = config["r2"]
        l = config["l"]
        a = config["a"]
        vf = view_factor(r1, r2, l, a)
        vf_library[config_name] = vf
        f.write(f"{config_name}: r1={r1}, r2={r2}, l={l}, a={a}, vf={vf}\n")