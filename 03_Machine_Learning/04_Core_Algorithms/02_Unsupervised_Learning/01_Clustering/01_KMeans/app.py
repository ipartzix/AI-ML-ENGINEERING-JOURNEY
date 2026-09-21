import matplotlib.pyplot as plt
import pandas as pd
from kmeans import KMeans

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/refs/heads/main/kmeans/student_clustering.csv')
X = df.iloc[:, :].values

# 1. Run Elbow Method to find optimal K
wcss = []
k_range = range(1, 11)

for k in k_range:
    km = KMeans(n_clusters=k, max_iter=500)
    km.fit_predict(X)
    wcss.append(km.inertia_)

# Plot Elbow Curve
plt.figure(figsize=(6, 4))
plt.plot(k_range, wcss, marker='o')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS / Inertia')
plt.grid(True)
plt.show()

# 2. Fit K-Means with optimal K (e.g., k = 4 based on the elbow point)
optimal_k = 4
km = KMeans(n_clusters=optimal_k, max_iter=500)
y_means = km.fit_predict(X)

# 3. Dynamically plot all clusters
plt.figure(figsize=(8, 5))
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta', 'lime', 'pink']

for cluster_id in range(optimal_k):
    plt.scatter(
        X[y_means == cluster_id, 0], 
        X[y_means == cluster_id, 1], 
        color=colors[cluster_id % len(colors)], 
        label=f'Cluster {cluster_id}'
    )

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title(f'Student Clusters (K={optimal_k})')
plt.legend()
plt.show()