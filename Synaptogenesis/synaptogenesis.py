import pygame
import numpy as np
import sys
import math


# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



array_space = np.zeros((100, 100, 100)) # Creates a 100^3 area space.


vertices = [
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [1, -1, 1],
    [-1, 1, 1],
    [-1, -1, 1],
    [-1, -1, -1],
    [-1, 1, -1]
]

# Define edges between the vertices
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 7),
    (2, 6),
    (3, 5)
]



def rotate_point(point, angle):
    x, y, z = point
    # Rotate around Y-axis
    cos_theta, sin_theta = math.cos(angle), math.sin(angle)
    x, z = x * cos_theta - z * sin_theta, x * sin_theta + z * cos_theta
    return [x, y, z]



def project_point(point):
    x, y, z = point
    # Simple perspective projection
    factor = 200 / (z + 5)
    x, y = x * factor, y * factor
    return int(WIDTH / 2 + x), int(HEIGHT / 2 - y)




def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Rotate and project points
        rotated_vertices = [rotate_point(v, angle) for v in vertices]
        projected_points = [project_point(v) for v in rotated_vertices]

        # Draw edges
        for edge in edges:
            pygame.draw.line(screen, WHITE, projected_points[edge[0]], projected_points[edge[1]], 2)

        angle += 0.01  # Increase the angle for the next frame
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()



