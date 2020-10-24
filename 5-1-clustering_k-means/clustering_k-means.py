# Clustering using k-Means
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

# TODO number of clusters to be used in k-Means
NUM_CLUSTERS = ...

# make sure that random selection of clusters always happens in the same order
# (to avoid plotting with different colors in subsequent runs)
np.random.seed(42)

# read wholesale data
df = pd.read_csv('wholesale_customers_data.csv', sep=',')
data = scale(df)

# TODO reduce dataset to two principal axes (for 2D plotting)
reduced_data = ...

# TODO run k-Means with selected number of clusters
kmeans = ...

# do not worry about all the fancy plotting down there, this is just for visualization,
# but doesn't add anything to the method

# step size of the mesh - smaller value -> higher sampling quality
h = .01

# get the decision boundaries between the clusters
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# get the cluster label for each point in the graph
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# plot the results
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# centroids (= cluster centers) should appear as white X -> "X marks the spot"
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)
plt.title('K-means clustering on the dataset (PCA-reduced data)\n'
          'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
