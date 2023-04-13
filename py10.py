import random
import math
import pandas as pd
import matplotlib.pyplot as plt

# Problem Eqn
def view_factor(r,h,l):
    L = l / r
    H = h / r
    X = (1 + H) ** 2 + L * L
    Y = (1 - H) ** 2 + L * L
    vf = (L / (math.pi * H)) *((1 / L) * math.atan(L / math.sqrt(H * H - 1)) +
          ((X - 2 * H) / math.sqrt(X * Y)) *
            math.atan(math.sqrt((X * (H - 1)) / (Y * (H + 1)))) -
          math.atan(math.sqrt((H - 1) / (H + 1))))
    return vf


# Generate Random Data
data = {'r': [], 'h': [], 'l': [], 'view_factor': []}
for i in range(100):
    r = random.uniform(0.1, 10.0)
    h = random.uniform(2 * r, 5.0 * r)
    l = random.uniform(0.1 * r, 5.0 * r)
    vf = view_factor(r, h, l)
    data['r'].append(r)
    data['h'].append(h)
    data['l'].append(l)
    data['view_factor'].append(vf)

df = pd.DataFrame(data)

# Plot view factor data
plt.scatter(df['h'], df['view_factor'])
plt.xlabel('h')
plt.ylabel('View Factor')
plt.ylim(0, 1.0)
plt.title('View Factor vs. h')
plt.savefig('10_view_factor_graph.png')

# Save data to Excel file
df.to_excel('10_view_factor_data.xlsx', index=False)
