import random
import math
import pandas as pd
import matplotlib.pyplot as plt

# Problem Eqn
def view_factor(w,h,l):
    H = h / l
    W = w / l
    W2 = W * W
    H2 = H * H
    vf1 = 1.0 / (3.141592653589793 * W)
    vf2 = (
        0.25
        * math.log(
            (((1 + W2) * (1 + H2)) / (1 + W2 + H2))
            * ((W2 * (1 + W2 + H2)) / ((1 + W2) * (W2 + H2))) ** W2
            * ((H2 * (1 + W2 + H2)) / ((1 + H2) * (W2 + H2))) ** H2
        )
        - math.sqrt(H2 + W2) * math.atan(1 / math.sqrt(H2 + W2))
        + W * math.atan(1 / W)
        + H * math.atan(1 / H)
    )
    return vf1 * vf2


# Generate Random Data
data = {'w': [], 'h': [], 'l': [], 'view_factor': []}
for i in range(100):
    w = random.uniform(0.1, 10.0)
    h = random.uniform(0.1 * w, 5.0 * w)
    l = random.uniform(0.1 * w, 5.0 * w)
    vf = view_factor(w, h, l)
    data['w'].append(w)
    data['h'].append(h)
    data['l'].append(l)
    data['view_factor'].append(vf)

df = pd.DataFrame(data)

# Plot view factor data
plt.scatter(df['l'], df['view_factor'])
plt.xlabel('l')
plt.ylabel('View Factor')
plt.ylim(0, 1.0)
plt.title('View Factor vs. l')
plt.savefig('02_view_factor_graph.png')

# Save data to Excel file
df.to_excel('02_view_factor_data.xlsx', index=False)
