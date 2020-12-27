import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange
plt.style.use('ggplot')

R = 1
xc = 0
yc = 0

def generate_1_point():
    # polar coordinates
    theta = np.random.random() * np.pi * 2
    return theta

def polar_to_cartesian(theta):
    x = R * np.cos(theta)
    y = R * np.sin(theta)
    return x, y

def is_center_in(theta_list):
    x1, y1 = polar_to_cartesian(theta_list[0])
    x2, y2 = polar_to_cartesian(theta_list[1])
    x3, y3 = polar_to_cartesian(theta_list[2])
    vec_1 = np.array([x2 - x1, y2 - y1])
    vec_2 = np.array([x3 - x2, y3 - y2])
    vec_3 = np.array([x1 - x3, y1 - y3])
    # test vec
    # 1
    vec_t = np.array([xc - x1, yc - y1])
    flag = np.cross(vec_1, vec_t)
    if flag == 0:
        return True
    # 2
    vec_t = np.array([xc - x2, yc - y2])
    flag = np.cross(vec_2, vec_t) * flag
    if flag == 0:
        return True
    if flag < 0:
        return False
    # 3
    vec_t = np.array([xc - x3, yc - y3])
    flag = np.cross(vec_3, vec_t) * flag
    if flag == 0:
        return True
    if flag < 0:
        return False
    return True

def main():
    CNT = 3000
    list_30 = []
    for _ in trange(30):
        cnt = 0
        per_list = []
        for i in range(CNT):
            theta_list = [generate_1_point() for _ in range(3)]
            if is_center_in(theta_list):
                cnt += 1
            # print("{:.5f}".format(cnt / (i + 1)))
            per_list.append(cnt / (i + 1))
        list_30.append(per_list)
    for per_list in list_30:
        plt.plot(per_list)
    plt.show()

if __name__ == "__main__":
    main()
