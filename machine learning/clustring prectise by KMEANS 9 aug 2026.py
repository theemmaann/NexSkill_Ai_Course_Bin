import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X=np.random.rand(100,2)

plt.figure(figsize=(7.5,3.5))
plt.scatter(X[:,0], X[:,1], s=20, cmap='summer');
plt.show()

Kmeans=KMeans(n_clusters=3,max_iter=100)
Kmeans.fit(X)

plt.figure(figsize=(7.5,3.5))
plt.scatter(X[:,0], X[:,1],c=Kmeans.labels_ ,s=20, cmap='summer');
plt.scatter(Kmeans.cluster_centers_[:,0], Kmeans.cluster_centers_[:,1], marker='s', c='r',s=50,alpha=0.9)
plt.show()


