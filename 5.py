import numpy as np
import open3d as o3d
import copy
from matplotlib import pyplot as plt
def draw_labels_on_model(pcl, labels):
    cmap = plt.get_cmap("tab20")
    pcl_temp = copy.deepcopy(pcl)
    max_label = labels.max()
    colors = cmap(labels / (max_label if max_label > 0 else 1))
    pcl_temp.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcl_temp], window_name="Result", width=800, height=600)
    o3d.io.write_point_cloud("Result11.pcd", pcl_temp)
def euclidean_distance(one_sample, X):
    one_sample = one_sample.reshape(1, -1)
    X = X.reshape(X.shape[0], -1)
    distances = np.power(np.tile(one_sample, (X.shape[0], 1)) - X, 2).sum(axis=1)
    return distances
class Kmeans(object):
    def __init__(self, k=2, max_iterations=1500, tolerance=0.01):
        self.k = k
        self.max_iterations = max_iterations
        self.tolerance = tolerance
    def init_random_centroids(self, X):
        n_samples, n_features = np.shape(X)
        centroids = np.zeros((self.k, n_features))
        for i in range(self.k):
            centroid = X[np.random.choice(range(n_samples))]
            centroids[i] = centroid
        return centroids
    def closest_centroid(self, sample, centroids):
        distances = euclidean_distance(sample, centroids)
        closest_i = np.argmin(distances)
        return closest_i
    def create_clusters(self, centroids, X):
        clusters = [[] for _ in range(self.k)]
        for sample_i, sample in enumerate(X):
            centroid_i = self.closest_centroid(sample, centroids)
            clusters[centroid_i].append(sample_i)
        return clusters
    def update_centroids(self, clusters, X):
        n_features = np.shape(X)[1]
        centroids = np.zeros((self.k, n_features))
        for i, cluster in enumerate(clusters):
            centroid = np.mean(X[cluster], axis=0)
            centroids[i] = centroid
        return centroids
    def get_cluster_labels(self, clusters, X):
        y_pred = np.zeros(np.shape(X)[0])
        for cluster_i, cluster in enumerate(clusters):
            for sample_i in cluster:
                y_pred[sample_i] = cluster_i
        return y_pred
    def predict(self, X):
        centroids = self.init_random_centroids(X)
        for _ in range(self.max_iterations):
            clusters = self.create_clusters(centroids, X)
            former_centroids = centroids
            centroids = self.update_centroids(clusters, X)
            diff = centroids - former_centroids
            if diff.any() < self.tolerance:
                break
        return self.get_cluster_labels(clusters, X)
if __name__ == "__main__":
    pcd = o3d.io.read_point_cloud("Original.pcd")
    points = np.asarray(pcd.points)
    o3d.visualization.draw_geometries([pcd], window_name="可视化原始点云", width=800, height=600)
    clf = Kmeans(k=100)
    labels = clf.predict(points)
    draw_labels_on_model(pcd, labels)

