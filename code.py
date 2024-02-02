import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from pandas.plotting import parallel_coordinates
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN

# Step 1: Loading the Wholesale customers dataset
data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv")

# Examine the structure of the dataset
data.head()

# Data exploration
# Checking the size of the dataset (number of rows and columns)
print("Dataset size:", data.shape, "\n")

# Displaying summary statistics of the dataset
print("Summary statistics:", "\n")
data.describe()

# Step 2: Data preprocessing
# Check for missing values
print(data.isnull().sum())

# Normalizing the data
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

# Converting the normalized data array back to a DataFrame
data_normalized = pd.DataFrame(normalized_data, columns=data.columns)

# Print the summary statistics of the normalized data
print("Summary statistics of normalized data:", "\n")
data_normalized.describe()

# Step 3: Finding the optimal number of clusters using the Silhouette coefficient
max_clusters = 10  # Maximum number of clusters to test
best_silhouette_score = -1
optimal_clusters = 2
silhouette_scores = []

for k in range(2, max_clusters+1):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(data_normalized)
    labels = kmeans.labels_
    silhouette_avg = silhouette_score(data_normalized, labels)
    silhouette_scores.append(silhouette_avg)
    if silhouette_avg > best_silhouette_score:
        best_silhouette_score = silhouette_avg
        optimal_clusters = k

print("Optimal number of clusters:", optimal_clusters)

# Plotting the silhouette scores for different numbers of clusters
plt.plot(range(2, max_clusters+1), silhouette_scores)
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Coefficient')
plt.title('Silhouette Method')
plt.show()

# Step 4: Applying the K-means clustering algorithm
kmeans = KMeans(n_clusters=optimal_clusters, n_init=10, random_state=42)

# Fit K-means to the preprocessed dataset
kmeans.fit(data_normalized)
labels = kmeans.labels_

# Visualize the results of the clustering algorithm
# Add the cluster labels to the original DataFrame
data['Cluster'] = kmeans.labels_

# Normalize the cluster labels for better visualization
data['Cluster'] = data['Cluster'].astype('category').cat.codes

sorted_data = data.sort_values('Cluster')

# Plot parallel coordinate plots for all features
plt.figure(figsize=(12, 6))
parallel_coordinates(sorted_data, 'Cluster', colormap='viridis')
plt.xticks(rotation=90)
plt.title('K-means Clustering - Parallel Coordinate Plots')
plt.legend(title='Cluster')
plt.show()

# Step 5: Evaluating the quality of the clustering results

# Calculating the Silhouette Coefficient
silhouette_avg = silhouette_score(data_normalized, kmeans.labels_)
print("Silhouette Coefficient:", silhouette_avg)

# Step 6: Applying hierarchical clustering
hierarchical = AgglomerativeClustering(n_clusters=optimal_clusters)
hierarchical.fit(data_normalized)
hierarchical_labels = hierarchical.labels_

# Add hierarchical cluster labels to the original DataFrame
data['Hierarchical_Cluster'] = hierarchical_labels

# Normalize the hierarchical cluster labels for better visualization
data['Hierarchical_Cluster'] = data['Hierarchical_Cluster'].astype('category').cat.codes

# Plot parallel coordinate plots for all features based on hierarchical clustering
plt.figure(figsize=(12, 6))
parallel_coordinates(data.sort_values('Hierarchical_Cluster'), 'Hierarchical_Cluster', colormap='viridis')
plt.xticks(rotation=90)
plt.title('Hierarchical Clustering - Parallel Coordinate Plots')
plt.legend(title='Cluster')
plt.show()

# Applying DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(data_normalized)
dbscan_labels = dbscan.labels_

# Add DBSCAN cluster labels to the original DataFrame
data['DBSCAN_Cluster'] = dbscan_labels

# Normalize the DBSCAN cluster labels for better visualization
data['DBSCAN_Cluster'] = data['DBSCAN_Cluster'].astype('category').cat.codes

# Plot parallel coordinate plots for all features based on DBSCAN clustering
plt.figure(figsize=(12, 6))
parallel_coordinates(data.sort_values('DBSCAN_Cluster'), 'DBSCAN_Cluster', colormap='viridis')
plt.xticks(rotation=90)
plt.title('DBSCAN Clustering - Parallel Coordinate Plots')
plt.legend(title='Cluster')
plt.show()

# Step 7: Evaluating the quality of the clustering results

# Calculating the Silhouette Coefficient of Hierarchical Clustering
silhouette_avg_hierarchical = silhouette_score(data_normalized, hierarchical_labels)
print("Silhouette Coefficient (Hierarchical Clustering):", silhouette_avg_hierarchical)

# Calculating the Silhouette Coefficient of DBSCAN
silhouette_avg_dbscan = silhouette_score(data_normalized, dbscan_labels)
print("Silhouette Coefficient (DBSCAN):", silhouette_avg_dbscan)
