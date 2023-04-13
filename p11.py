import random
import math
import pandas as pd
import matplotlib.pyplot as plt

# Problem Eqn
def view_factor(r,z,l):
    L = l / r
    Z = z/ l
    X = (1 + L)
    Y = math.pow((X*X - 1),0.5)
    vf = 0.5 - ((1/3.141592)*(X - Y + math.atan(X + Y)- math.atan(X -Y)))
    return vf


# Generate Random Data
data = {'r': [], 'z': [], 'l': [], 'view_factor': []}
for i in range(100):
    r = random.uniform(0.1, 10.0)
    z = random.uniform(0.1 * r, 5.0 * r)
    l = random.uniform(0.1 * r, 5.0 * r)
    vf = view_factor(r, z, l)
    data['r'].append(r)
    data['z'].append(z)
    data['l'].append(l)
    data['view_factor'].append(vf)

df = pd.DataFrame(data)

# Plot view factor data
plt.scatter(df['l'], df['view_factor'])
plt.xlabel('l')
plt.ylabel('View Factor')
plt.ylim(0, 1.0)
plt.title('View Factor vs. l')
plt.savefig('11_view_factor_graph.png')

# Save data to Excel file
df.to_excel('11_view_factor_data.xlsx', index=False)
