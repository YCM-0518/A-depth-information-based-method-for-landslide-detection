import open3d as o3d
import numpy as np
def read_pcd(file_path):
	pcd = o3d.io.read_point_cloud(file_path)
	points = np.asarray(pcd.points)
	return points
point = read_pcd("Original.pcd")
with open('Denoising.txt','w',encoding='utf-8') as f:
	for i in range(len(point)):
		x = point[i][0]
		y = point[i][1]
		z = point[i][2]
		if  x <= 0.33 and x >= -0.42 and y <= -0.57 and y >= -1.37:
			points = str(x)+' '+str(y)+' '+str(z) + '\n'
			f.write(points)
f.close()
