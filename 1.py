import open3d as o3d
import numpy as np
import copy
Original = o3d.io.read_point_cloud("Original.pcd")
target = copy.deepcopy(Original)
#b = 30
b = 60
a = (90 - b)
rad = a / 180 * np.pi
target.transform(np.array([[1.0, 0.0, 0.0, 0.0],
                           [0.0, np.cos(rad), -np.sin(rad), 0.0],
                           [0.0, np.sin(rad), np.cos(rad), 0.0],
                           [0.0, 0.0, 0.0, 1.0]]))
o3d.io.write_point_cloud("target.pcd", target)
