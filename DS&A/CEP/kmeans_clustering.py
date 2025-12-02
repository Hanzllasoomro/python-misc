# Task 4: K-Means clustering + elbow + 2D plot
# Requirements: pip install pandas scikit-learn matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.decomposition import PCA

df = pd.read_csv("StudentsPerformance.csv")
X = df[['math score','reading score','writing score']].values

# 4c) Elbow method (fast version)
ks = range(1, 11)
inertias = []
for k in ks:
    km = MiniBatchKMeans(n_clusters=k, random_state=42, n_init=5, batch_size=128)
    km.fit(X)
    inertias.append(km.inertia_)

plt.figure()
plt.plot(list(ks), inertias, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia (within-cluster SSE)')
plt.tight_layout()
plt.savefig("task4_elbow.png")
plt.show()

# 4a) Choose k (inspect the elbow; 3 is a common choice on this dataset)
k = 3  # adjust if your elbow suggests differently

km = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = km.fit_predict(X)
df['cluster'] = labels

# 4b) Plot clusters in 2D via PCA (for visualization only)
pca = PCA(n_components=2, random_state=42)
X2 = pca.fit_transform(X)

plt.figure()
plt.scatter(X2[:,0], X2[:,1], c=df['cluster'])
plt.title(f'K-Means Clusters (k={k}) in PCA(2D) space')
plt.xlabel('PC1'); plt.ylabel('PC2')
plt.tight_layout()
plt.savefig("task4_clusters.png")
plt.show()

# 4d) Inspect/interpret centers (original score scale)
centers = pd.DataFrame(km.cluster_centers_,
                       columns=['math score','reading score','writing score']).round(2)
print("Cluster centers (original score units):\n", centers)
