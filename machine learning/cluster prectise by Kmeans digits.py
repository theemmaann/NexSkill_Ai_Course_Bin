import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans

digits=load_digits()
print('digits.data.shape():', digits.data.shape)
print()

Kmeans=KMeans(n_clusters=10,random_state=0)
cluster=Kmeans.fit_predict(digits.data)
Kmeans.cluster_centers_.shape
print('Kmeans.cluster_center_.shape:', Kmeans.cluster_centers_.shape)

fig, ax =plt.subplots(2,5, figsize=(8,3))
centers=Kmeans.cluster_centers_.reshape(10,8,8)
for axi, center in zip(ax.flat,centers):
    axi.set(xticks=[], yticks=[])
    axi.imshow(center,interpolation='nearest', cmap=plt.cm.binary)
fig.show()    

from scipy.stats import mode
labels=np.zeros_like(cluster)
for i in range(10):
    mask=(cluster==i)
    labels[mask]=mode(digits.target[mask])[0]
from sklearn.metrics import accuracy_score
print('accuracy score:', accuracy_score(digits.target,labels))    
