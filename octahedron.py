import pygame


class Octahedron:

    def __init__(self):
        self.octahedron_points = [
            [[0], [0], [1]],
            [[1], [0], [0]],
            [[0], [0], [-1]],
            [[-1], [0], [0]],
            [[0], [1], [0]],
            [[0], [-1], [0]]
        ]
        self.faces = [
            (0, 1, 5),
            (1, 2, 5),
            (2, 3, 5),
            (3, 0, 5),
            (1, 0, 4),
            (2, 1, 4),
            (3, 2, 4),
            (0, 3, 4)
        ]

    def get_octahedron_points(self):
        return self.octahedron_points

    def get_faces(self):
        return self.faces

    @classmethod
    def draw(cls, points, window):
        cls.__draw_line(0, 1, points, window)
        cls.__draw_line(1, 2, points, window)
        cls.__draw_line(2, 3, points, window)
        cls.__draw_line(0, 3, points, window)
        cls.__draw_line(0, 5, points, window)
        cls.__draw_line(1, 5, points, window)
        cls.__draw_line(2, 5, points, window)
        cls.__draw_line(3, 5, points, window)
        cls.__draw_line(0, 4, points, window)
        cls.__draw_line(1, 4, points, window)
        cls.__draw_line(2, 4, points, window)
        cls.__draw_line(3, 4, points, window)

    @classmethod
    def __draw_line(cls, i, j, points, window):
        pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))
