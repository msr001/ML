import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Data: [Age, Income]
X = [[20,20000],[25,32000],[26,35000],[28,40000],[30,50000],
     [35,60000],[40,80000],[45,98000],[50,118000],[55,145000],[60,138000]]


m = KMeans(n_clusters=3)
m.fit(X)   

age = [i[0] for i in X]
income = [i[1] for i in X]

plt.scatter(age, income, c=m.labels_)


plt.scatter(m.cluster_centers_[:,0],
            m.cluster_centers_[:,1],
            marker="X", s=100, color="red")

plt.xlabel("Age")
plt.ylabel("Income")
plt.title("K Means Clustering Graph")

plt.show()
