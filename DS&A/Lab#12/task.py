# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Step 1: Generate sample data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Step 2: Visualize the data (without labels, since it's unsupervised)
plt.scatter(X[:, 0], X[:, 1], s=30, color='gray')
plt.title("Unlabeled Data (Before Clustering)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Step 3: Apply K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)

# Step 4: Get cluster centroids and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Step 5: Visualize clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.7, marker='X', label='Centroids')
plt.title("K-Means Clustering Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
