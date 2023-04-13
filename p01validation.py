import math


# Problem Eqn
def view_factor(a,b,c):
    B = b / a
    C = c / a
    BpC = B + C
    BmC = C - B
    F12 = math.sqrt(BpC * BpC + 4) - math.sqrt(BmC * BmC + 4)
    return F12 / (2 * B)

# Define input configurations
configs = {
    "config1": {"a": 1, "b": 1, "c": 1},
    "config2": {"a": 1, "b": 2, "c": 3},
    "config3": {"a": 2, "b": 2, "c": 2},
    "config4": {"a": 2, "b": 3, "c": 4},
    "config5": {"a": 1, "b": 3, "c": 5},
    "config6": {"a": 5, "b": 7, "c": 9},
    "config7": {"a": 2, "b": 4, "c": 6},
    "config8": {"a": 6, "b": 8, "c": 10},
    "config9": {"a": 1, "b": 9, "c": 5},
    "config10": {"a": 4, "b": 2, "c": 5},
    # add more configurations here...
}

# Calculate view factors for each configuration
vf_library = {}
for config_name, config in configs.items():
    a = config["a"]
    b = config["b"]
    c = config["c"]
    vf = view_factor(a, b, c)
    vf_library[config_name] = vf

# Print library
print(vf_library)

# Save library into txt file
with open("01_vf_validation.txt", "w") as f:
    for config_name, config in configs.items():
        a = config["a"]
        b = config["b"]
        c = config["c"]
        vf = view_factor(a, b, c)
        vf_library[config_name] = vf
        f.write(f"{config_name}: a={a}, b={b}, c={c}, vf={vf}\n")

