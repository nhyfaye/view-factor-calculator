import math
import random
import pandas as pd
import matplotlib.pyplot as plt


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
    return max(0.0, min(vf, 1.0)) # ensure vf is between 0.0 and 1.0

a_min = 10
r1_min = 5
r2_min = 10
l_min = 1
a_max = 50
r1_max = 2
r2_max = 30
l_max = 10

data = []
for i in range(100):
    a = random.uniform(a_min, a_max)
    r1 = random.uniform(r1_min, r2_min)
    r2 = random.uniform(r1, r2_max)
    l = random.uniform(l_min, l_max)
    vf = view_factor(r1, r2, l, a)
    data.append((a, r1, r2, l, vf))

# Save data to Excel file
df = pd.DataFrame(data, columns=["a", "r1", "r2", "l", "view_factor"])
df.to_excel("12_view_factor_data.xlsx", index=False)

# Plot view factor data
plt.scatter(df.index, df["view_factor"])
plt.title("View Factor Data")
plt.xlabel("Sample")
plt.ylabel("View Factor")
plt.ylim(0, 1)
plt.savefig("12_view_factor_graph.png")
plt.show()
