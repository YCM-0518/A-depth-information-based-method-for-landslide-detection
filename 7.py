import open3d as o3d
import numpy as np
def pca_compute(data, sort=True):
    average_data = np.mean(data, axis=0)
    decentration_matrix = data - average_data
    H = np.dot(decentration_matrix.T, decentration_matrix)
    eigenvectors, eigenvalues, eigenvectors_T = np.linalg.svd(H)
    if sort:
        sort = eigenvalues.argsort()[::-1]
        eigenvectors = eigenvectors[:, sort]
    return eigenvectors, average_data
if __name__ == '__main__':
    pcd = o3d.io.read_point_cloud("Original.pcd")
    points = np.asarray(pcd.points)
    v, c = pca_compute(points)
    coefficients = v[:, 2]
    A = coefficients[0]
    B = coefficients[1]
    C = coefficients[2]
    D = -(A * c[0] + B * c[1] + C * c[2])
    print('Equation：%.6f * x + %.6f * y + %.6f*z + %.6f = 0' % (A, B, C, D))
