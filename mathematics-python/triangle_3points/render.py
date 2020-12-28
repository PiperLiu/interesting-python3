import numpy as np
import matplotlib.pyplot as plt
import sys
from numpy.core.numerictypes import ScalarType
import pygame
from pygame.locals import *
plt.style.use('ggplot')

R = 1
xc = 0
yc = 0

pygame.init()
pygame.display.set_caption("Piper蛋窝")
screen = pygame.display.set_mode((360, 240))
fcclock = pygame.time.Clock()

SCALE = 80
FPS   = 10

total_score = 0
isin_socre  = 0

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
    flag1 = np.cross(vec_1, vec_t)
    if flag1 == 0:
        return True
    # 2
    vec_t = np.array([xc - x2, yc - y2])
    flag2 = np.cross(vec_2, vec_t)
    if flag2 == 0:
        return True
    # 3
    vec_t = np.array([xc - x3, yc - y3])
    flag3 = np.cross(vec_3, vec_t)
    if flag3 == 0:
        return True
    if (flag1 > 0 and flag2 > 0 and flag3 > 0) or \
            (flag1 < 0 and flag2 < 0 and flag3 < 0):
        return True
    return False

def draw_static():
    pygame.draw.circle(screen,
                       (255, 255, 255),
                       (360 // 3, 240 // 2),
                       R * SCALE,
                       3)
    pygame.draw.circle(screen,
                       (255, 255, 255),
                       (360 // 3, 240 // 2),
                       5)

def draw_dynamic(theta_list):
    global isin_socre
    xc_draw = 360 // 3
    yc_draw = 240 // 2
    x1, y1 = polar_to_cartesian(theta_list[0])
    x2, y2 = polar_to_cartesian(theta_list[1])
    x3, y3 = polar_to_cartesian(theta_list[2])
    x1, y1 = x1 * SCALE + xc_draw, y1 * SCALE + yc_draw
    x2, y2 = x2 * SCALE + xc_draw, y2 * SCALE + yc_draw
    x3, y3 = x3 * SCALE + xc_draw, y3 * SCALE + yc_draw
    # is in
    flag = is_center_in(theta_list)
    if flag:
        isin_socre += 1
    # draw
    r_point = 6
    l_width = 4
    inColor_r = (123, 104, 238)
    inColor_l = (147, 112, 219)
    notinColor_r = (199, 21, 133)
    notinColor_l = (218, 112, 214)
    pygame.draw.circle(screen,
                       inColor_r if flag else notinColor_r,
                       (int(x1), int(y1)),
                       r_point)
    pygame.draw.circle(screen,
                       inColor_r if flag else notinColor_r,
                       (int(x2), int(y2)),
                       r_point)
    pygame.draw.circle(screen,
                       inColor_r if flag else notinColor_r,
                       (int(x3), int(y3)),
                       r_point)
    # line
    pygame.draw.line(screen,
                     inColor_l if flag else notinColor_l,
                     (int(x1), int(y1)),
                     (int(x2), int(y2)),
                     l_width)
    pygame.draw.line(screen,
                     inColor_l if flag else notinColor_l,
                     (int(x2), int(y2)),
                     (int(x3), int(y3)),
                     l_width)
    pygame.draw.line(screen,
                     inColor_l if flag else notinColor_l,
                     (int(x3), int(y3)),
                     (int(x1), int(y1)),
                     l_width)

def draw_score():
    global total_score
    global isin_socre
    WHITE = (255, 255, 255)
    text_1 = pygame.font.Font('freesansbold.ttf', 30)
    text_1_surface = text_1.render(str(isin_socre), True, WHITE)
    text_1_rect    = text_1_surface.get_rect()
    text_1_rect.center = (360 // 20 * 13, 240 // 10 * 4)
    screen.blit(
        text_1_surface,
        text_1_rect
    )
    text_2 = pygame.font.Font('freesansbold.ttf', 30)
    text_2_surface = text_2.render(str(total_score), True, WHITE)
    text_2_rect    = text_2_surface.get_rect()
    text_2_rect.center = (360 // 20 * 13, 240 // 10 * 6)
    screen.blit(
        text_2_surface,
        text_2_rect
    )
    pygame.draw.line(screen,
                     WHITE,
                     (360 // 20 * 12, 240 // 10 * 5),
                     (360 // 20 * 14, 240 // 10 * 5),
                     3)
    text_3 = pygame.font.Font('freesansbold.ttf', 30)
    text_3_surface = text_3.render('=', True, WHITE)
    text_3_rect    = text_3_surface.get_rect()
    text_3_rect.center = (360 // 20 * 15, 240 // 10 * 5)
    screen.blit(
        text_3_surface,
        text_3_rect
    )
    text_4 = pygame.font.Font('freesansbold.ttf', 30)
    text_4_surface = text_4.render('{:.2f}'.format(isin_socre / total_score), True, WHITE)
    text_4_rect    = text_4_surface.get_rect()
    text_4_rect.center = (360 // 40 * 35, 240 // 50 * 31)
    screen.blit(
        text_4_surface,
        text_4_rect
    )

def draw(theta_list):
    screen.fill((0, 0, 0))
    draw_static()
    draw_dynamic(theta_list)
    draw_score()
    fcclock.tick(FPS)
    pygame.display.update()

def main():
    global total_score
    pygame.init()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
        theta_list = [generate_1_point() for _ in range(3)]
        total_score += 1
        draw(theta_list)

if __name__ == "__main__":
    main()
