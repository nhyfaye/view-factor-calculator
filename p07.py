import random
import math
import pandas as pd
import matplotlib.pyplot as plt

# Problem Eqn
def view_factor(r1,r2,h):
    R = r2 / r1
    H = h / r1
    vf = (1 / R) * (1 -
          (H * H + R * R - 1) / (4 * H) -
          (1 / math.pi) *
            (math.acos((H * H - R * R + 1) / (H * H + R * R - 1)) -
              (math.sqrt((H * H + R * R + 1) ** 2 - 4 * R * R) / (2 * H)) *
                math.acos((H * H - R * R + 1) / (R * (H * H + R * R - 1))) -
              ((H * H - R * R + 1) / (2 * H)) * math.asin(1 / R)));
    return vf


# Generate Random Data
data = {'r1': [], 'r2': [], 'h': [], 'view_factor': []}
for i in range(100):
    r1 = random.uniform(0.1, 10.0)
    r2 = random.uniform(2 * r1, 5.0 * r1)
    h = random.uniform(0.1 * r1, 5.0 * r1)
    vf = view_factor(r1, r2, h)
    data['r1'].append(r1)
    data['r2'].append(r2)
    data['h'].append(h)
    data['view_factor'].append(vf)

df = pd.DataFrame(data)

# Plot view factor data
plt.scatter(df['h'], df['view_factor'])
plt.xlabel('h')
plt.ylabel('View Factor')
plt.ylim(0, 1.0)
plt.title('View Factor vs. h')
plt.savefig('07_view_factor_graph.png')

# Save data to Excel file
df.to_excel('07_view_factor_data.xlsx', index=False)
