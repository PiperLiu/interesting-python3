import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

def gen_data():
    mean_1 = [-1, 4]
    cov_1 = [[1, 8], [2, 10]]  # diagonal covariance
    class_1_data = np.random.multivariate_normal(mean_1, cov_1, 1000)

    mean_2 = [2, 1]
    cov_2 = [[3, 10], [0, 1]]  # diagonal covariance
    class_2_data = np.random.multivariate_normal(mean_2, cov_2, 1000)

    return class_1_data, class_2_data

def main():
    class_1_data, class_2_data = gen_data()
    x1, y1 = class_1_data.T
    x2, y2 = class_2_data.T
    plt.scatter(x1, y1, s=7)
    plt.scatter(x2, y2, s=7)
    # plt.axis('equal')
    plt.show()

main()
