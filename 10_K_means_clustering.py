import warnings; warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = [[20,20000],[25,32000],[26,35000],[28,40000],[30,50000],[35,60000],[40,80000],[45,98000],[50,118000],[55,145000],[60,138000]]

m = KMeans(n_clusters=3).fit(X)

plt.scatter(zip(X))
plt.scatter(m.clustercenters[:,0], m.clustercenters[:,1], marker="X", s=100)
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("K means clustering graph")
plt.show() 
