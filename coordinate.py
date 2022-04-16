import pygame


class Coordinate:

    def __init__(self):
        self.coordinate_points = [
            [[0.5], [0], [0]],
            [[0], [0.5], [0]],
            [[0], [0], [0.5]],
            [[0], [0], [0]]
        ]

    def get_coordinate_points(self):
        return self.coordinate_points

    @classmethod
    def draw(cls, points, window):
        cls.__draw_line(0, 3, points, window, (0, 0, 255))
        cls.__draw_line(1, 3, points, window, (0, 255, 0))
        cls.__draw_line(2, 3, points, window, (255, 0, 0))

    @classmethod
    def __draw_line(cls, i, j, points, window, color):
        pygame.draw.line(window, color, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
