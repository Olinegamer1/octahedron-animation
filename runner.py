import pygame

from controller import action
from coordinate import Coordinate
from octahedron import Octahedron
from tetrahedron import Tetrahedron

WINDOW_SIZE = 1200
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()

if __name__ == '__main__':
    octahedron = Octahedron()
    coordinate = Coordinate()
    tetrahedron = Tetrahedron()

    while True:
        clock.tick(144)
        for event in pygame.event.get():
            window.fill((0, 0, 0))
            action(event, tetrahedron, coordinate, window)
        pygame.display.update()
