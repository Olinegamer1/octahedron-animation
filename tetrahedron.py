import pygame


class Tetrahedron:

    def __init__(self):
        self.octahedron_points = [
            [[-1], [-1], [-1]],
            [[-1], [1], [1]],
            [[1], [-1], [1]],
            [[1], [1], [-1]]
        ]
        self.faces = [
            (0, 2, 1),
            (2, 0, 3),
            (1, 2, 3),
            (3, 0, 1)
        ]

    def get_octahedron_points(self):
        return self.octahedron_points

    def get_faces(self):
        return self.faces

    @classmethod
    def draw(cls, points, window):
        cls.__draw_line(0, 1, points, window)
        cls.__draw_line(0, 2, points, window)
        cls.__draw_line(1, 2, points, window)
        cls.__draw_line(1, 3, points, window)
        cls.__draw_line(0, 3, points, window)
        cls.__draw_line(2, 3, points, window)


    @classmethod
    def __draw_line(cls, i, j, points, window):
        pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))
