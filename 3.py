import open3d as o3d
pcd = o3d.io.read_point_cloud("Original.pcd")
cl, ind = pcd.remove_statistical_outlier(nb_neighbors=1100, std_ratio=1)
cloud = pcd.select_by_index(ind)
o3d.visualization.draw_geometries([cloud], window_name="Denoising")
o3d.io.write_point_cloud("Denoising.pcd", cloud)
