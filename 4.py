import open3d as o3d
import numpy as np
def display_inlier_outlier(cloud, m_ind):
    inlier_cloud = cloud.select_by_index(m_ind)
    outlier_cloud = cloud.select_by_index(m_ind, invert=True)
    outlier_cloud.paint_uniform_color([255, 0, 0])
    inlier_cloud.paint_uniform_color([0, 0, 255])
    pcd_combined = outlier_cloud + inlier_cloud
    o3d.io.write_point_cloud("Result.pcd", pcd_combined)
source = o3d.io.read_point_cloud("0riginal-1.pcd")
target = o3d.io.read_point_cloud("Original-0.pcd")
threshold = source.compute_point_cloud_distance(target)
threshold = np.asarray(threshold)
ind = np.where(threshold < 0.008)[0]
display_inlier_outlier(source, ind)
