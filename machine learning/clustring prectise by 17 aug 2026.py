import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

X,_=make_blobs(n_samples=50,centers=3,cluster_std=0.6,random_state=42)
print('X:', X)

plt.figure(figsize=(10,5))
dendogram=sch.dendrogram(sch.linkage(X,method='ward'))
plt.title('Dendogram(Tree diagram)')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distance')

model=AgglomerativeClustering(n_clusters=3,linkage='ward')
y_predict=model.fit_predict(X)
print('Cluster labels:', y_predict)   # confirms clustering actually ran

plt.figure(figsize=(8,6))
plt.scatter(X[:,0],X[:,1], c=y_predict,cmap='rainbow',s=20)
plt.title('Hierarchical Clustering Results')

plt.show()   # shows both figures together