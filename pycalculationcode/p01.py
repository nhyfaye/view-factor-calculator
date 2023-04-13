import random
import math
import pandas as pd
import matplotlib.pyplot as plt

# Problem Eqn
def view_factor(a,b,c):
    B = b / a
    C = c / a
    BpC = B + C
    BmC = C - B
    F12 = math.sqrt(BpC * BpC + 4) - math.sqrt(BmC * BmC + 4)
    return F12 / (2 * B)

# Generate Random Data
data = {'a': [], 'b': [], 'c': [], 'view_factor': []}
for i in range(100):
    a = random.uniform(0.1, 10.0)
    b = random.uniform(0.1 * a, 5.0 * a)
    c = random.uniform(0.1 * a, 5.0 * a)
    vf = view_factor(a, b, c)
    data['a'].append(a)
    data['b'].append(b)
    data['c'].append(c)
    data['view_factor'].append(vf)

df = pd.DataFrame(data)

# Plot view factor data
plt.scatter(df['a'], df['view_factor'])
plt.xlabel('a')
plt.ylabel('View Factor')
plt.ylim(0, 1.0)
plt.title('View Factor vs. a')
plt.savefig('01_view_factor_graph.png')

# Save data to Excel file
df.to_excel('01_view_factor_data.xlsx', index=False)
