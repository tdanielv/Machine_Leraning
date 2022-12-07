import pandas as pd
from neulab.Clustering import CGraphMST, CGraph
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
d = {'Age': [18, 33, 42, 24, 19, 25], 'Sex': [0, 1, 1, 0, 2, 2]}
df = pd.DataFrame(data=d, index=['A', 'B', 'C', 'D', 'E', 'F'])

clusters = CGraphMST(df,clst_num=2, metric='manhattan', rnd=3, draw=True, info=True)
clusters2 = CGraph(df,metric='manhattan', r='std', rnd=3, draw=True, info=True)

print(df)
import matplotlib.pyplot as plt

plt.scatter(df.Age, df.Sex, alpha = 0.6, s=10)
plt.show()
