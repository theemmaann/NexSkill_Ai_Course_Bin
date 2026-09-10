from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
print('X:', X)
plt.figure(figsize=(7.5,3.5))
plt.scatter(X[:,0], X[:,1], s=20, cmap='summer');
plt.show()



kmeans = KMeans(n_clusters=4, max_iter=100)
kmeans.fit(X)

plt.figure(figsize=(7.5, 3.5))
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=20, cmap='summer')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            marker='s', c='r', s=200, alpha=0.9)
plt.show()


from sklearn.datasets import make_circles
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, _ = make_circles(n_samples=100, random_state=0)
print('X:', X)

plt.figure(figsize=(2.4,7.5))
plt.scatter(X[:,0], X[:,1], s=20, cmap='summer')
plt.show()

kmeans = KMeans(n_clusters=4, max_iter=100)
kmeans.fit(X)          # <- yahan X pass karna zaroori tha

plt.figure(figsize=(2.4,7.5))
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, s=20, cmap='summer');
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='s', c='r', s=50, alpha=0.01)
plt.show()


import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans

X,_=make_moons(n_samples=100,random_state=0)
print('X:', X)

plt.figure(figsize=(12,10))
plt.scatter(X[:,0], X[:,1], s=20, cmap='summer')
plt.show()

kmeans=KMeans()
kmeans.fit(X)

plt.figure(figsize=(12,10))
plt.scatter(X[:,0], X[:,1],c=kmeans.labels_, cmap='summer' );
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='s', c='r', s=20, alpha=0.01)
plt.show()

from sklearn.datasets import make_biclusters
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

plt.figure(figsize=(10,5))
plt.scatter(X[:,0], X[:,1], s=20, cmap='summer')
plt.show()

kmeans=KMeans()
kmeans.fit(X)

plt.figure(figsize=(10,5))
plt.scatter(X[:,0], X[:,1],c=kmeans.labels_, cmap='summer');
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='s', c='r',s=20,alpha=0.01)


