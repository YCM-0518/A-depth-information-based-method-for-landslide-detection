import os
import open3d as o3d
import numpy as np
def batch_visual_point_cloud(pcd_path):
    files = os.listdir(pcd_path)
    for f in files:
        pcd = o3d.io.read_point_cloud(pcd_path + f)
        xyz = np.asarray(pcd.points)
        [x, y, z] = np.mean(xyz, axis=0)
        if z > (((0.051696 * x) + (-0.199762 * y) + (-1.811083))/(-0.978480)): #Original point cloud ---- Equation
            pcd.paint_uniform_color([1, 0, 0])
            o3d.io.write_point_cloud("C:/test/2/" + str(f), pcd)
        if z < (((0.051696 * x) + (-0.199762 * y) + (-1.811083))/(-0.978480)):
            pcd.paint_uniform_color([0, 0, 1])
            o3d.io.write_point_cloud("C:/test/2/" + str(f), pcd)
if __name__ == '__main__':
    batch_visual_point_cloud("C:/test/1/")
# Different areas are distinguished by point cloud color