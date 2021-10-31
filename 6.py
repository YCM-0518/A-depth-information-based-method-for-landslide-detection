import numpy as np
import open3d as o3d
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
pcd = o3d.io.read_point_cloud("Original.pcd")
data1 = np.asarray(pcd.points)
transfer = StandardScaler()
data_new = transfer.fit_transform(data1)
estimator = KMeans(n_clusters=100)
estimator.fit(data_new)
y_pred = estimator.predict(data_new)
for i in range(100):
    idx = np.where(y_pred == i)[0]
    cloud1 = pcd.select_by_index(idx)
    o3d.io.write_point_cloud(str(i) + ".pcd", cloud1)
