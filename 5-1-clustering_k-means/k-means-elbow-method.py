# Clustering using k-Means
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

# read wholesale data
df = pd.read_csv('wholesale_customers_data.csv', sep=',')
data = scale(df)

# TODO reduce dataset to two principal axes (for 2D plotting)
reduced_data = ...

# TODO run k-Means in a loop with increasing number of clusters to find the optimal one
inertias = []
# TODO K should be [2,15]
K = ...
for k in K:
    # TODO run k-Means with selected number of clusters
    kmeans = ...
    inertias.append(kmeans.inertia_)

plt.plot(K, inertias, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('Elbow method for optimal k')
plt.show()
