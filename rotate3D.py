import copy

import numpy as np
import pygame

from numpy import cos, sin

COLORS = {
    0: (0, 24, 137),
    1: (66, 4, 158),
    2: (106, 0, 168),
    3: (144, 13, 164),
    4: (177, 42, 144),
    5: (204, 70, 120),
    6: (225, 100, 98),
    7: (241, 132, 75),
    8: (252, 166, 54)
}


def rotate(figure_points, angle_x, angle_y, angle_z, window, scale=150):
    points = []

    rotation_x = [[1, 0, 0],
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]

    for index, point in enumerate(figure_points):
        rotate_x = np.dot(rotation_x, point)
        rotate_y = np.dot(rotation_y, rotate_x)
        rotate_z = np.dot(rotation_z, rotate_y)

        x = (rotate_z[0][0] * scale) + np.mean(window.get_size()) / 2
        y = (rotate_z[1][0] * scale) + np.mean(window.get_size()) / 2
        z = (rotate_z[2][0] * scale) + np.mean(window.get_size()) / 2
        points.append([x, y, z])
    return points


def __createFace(points, index, window):
    a, b, c = points[0], points[1], points[2]

    v1 = b[0] - a[0], b[1] - a[1], b[2] - a[2]
    v2 = c[0] - a[0], c[1] - a[1], c[2] - a[2]
    n = np.cross(v1, v2)
    if n[2] > 0:
        return
    coords = ((b[0], b[1]), (a[0], a[1]), (c[0], c[1]))
    pygame.draw.polygon(window, COLORS[index], coords)


def render_faces(points, octahedron, window):
    coords = copy.copy(points)
    for index, face in enumerate(octahedron.get_faces()):
        __createFace((coords[face[0]], coords[face[1]], coords[face[2]]), index, window)
