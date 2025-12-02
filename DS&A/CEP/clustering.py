from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Step 1 — Load and clean the data
df = pd.read_csv("StudentsPerformance.csv")
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]   # normalize names

# Step 2 — Select features for clustering
X_scores = df[["math_score", "reading_score", "writing_score"]].values

# Step 3 — Scale features
X_scores_s = StandardScaler().fit_transform(X_scores)

# Step 4 — Elbow method to find optimal k
ks = range(1, 11)
inertias = []
for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X_scores_s)
    inertias.append(km.inertia_)

plt.figure()
plt.plot(ks, inertias, marker="o")
plt.title("Elbow Method: Inertia vs k")
plt.xlabel("k (number of clusters)")
plt.ylabel("Inertia")
plt.xticks(ks)
plt.tight_layout()
plt.savefig("elbow_method.png", dpi=150)
plt.show()

# Step 5 — Choose k (heuristic or visual inspection)
k_opt = 3
for i in range(1, len(inertias)):
    if (inertias[i-1] - inertias[i]) / inertias[i-1] < 0.10:
        k_opt = ks[i]
        break
print("Chosen k:", k_opt)

# Step 6 — Fit final K-Means and attach cluster labels
kmeans = KMeans(n_clusters=k_opt, n_init=10, random_state=42)
df["cluster"] = kmeans.fit_predict(X_scores_s)

# Step 7 — 2-D PCA projection for visualization
X2 = PCA(n_components=2, random_state=42).fit_transform(X_scores_s)
plt.figure()
for cl in np.unique(df["cluster"]):
    idx = df["cluster"] == cl
    plt.scatter(X2[idx, 0], X2[idx, 1], s=25, label=f"Cluster {cl}")
plt.title(f"K-Means Clusters (k = {k_opt}) — PCA projection")
plt.xlabel("PC1"); plt.ylabel("PC2")
plt.legend()
plt.tight_layout()
plt.savefig("kmeans_clusters_pca.png", dpi=150)
plt.show()

# Step 8 — Cluster means summary
summary = (
    df.groupby("cluster")[["math_score","reading_score","writing_score"]]
      .mean()
      .round(2)
)
print("\nCluster mean scores:\n", summary)
summary.to_csv("cluster_summary.csv")
