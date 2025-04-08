import pygame
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
RADIUS = 150
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab2Ex1")

def draw_polygon(surface, transform_matrix, translate=(0, 0)):
    center = (WIDTH // 2 + translate[0], HEIGHT // 2 + translate[1])
    num_vertices = 14
    points = []
    for i in range(num_vertices):
        angle = i * 2 * math.pi / num_vertices
        x, y = RADIUS * math.cos(angle), RADIUS * math.sin(angle)
        transformed_x = transform_matrix[0][0] * x + transform_matrix[0][1] * y + center[0]
        transformed_y = transform_matrix[1][0] * x + transform_matrix[1][1] * y + center[1]
        points.append((transformed_x, transformed_y))
    pygame.draw.polygon(surface, RED, points)

transformations = [
    [[1, 0], [0, 1]],
    [[math.cos(math.pi/4) * 2, -math.sin(math.pi/4) * 2], [math.sin(math.pi/4) * 2, math.cos(math.pi/4) * 2]],
    [[-1, 0], [0, 2]],
    [[math.cos(-math.pi/4) * 2, -math.sin(-math.pi/4) * 2], [math.sin(-math.pi/4) * 2, math.cos(-math.pi/4) * 2]],
    [[2, 0], [0, 1]],
    [[0, -1], [1, 1]],
    [[-1, 0], [0, 2]],
    [[math.cos(5*math.pi/4), -math.sin(5*math.pi/4)], [math.sin(5*math.pi/4), math.cos(5*math.pi/4)]],
    [[-1, 0.5], [0, -1]]
]

translations = [
    (0, 0), (0, 0), (0, 0), (0, 0), (0, -50), (0, 0), (0, 0), (0, 0), (100, 0)
]

running = True
transform_index = 0
while running:
    screen.fill(YELLOW)
    draw_polygon(screen, transformations[transform_index], translations[transform_index])
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                transform_index = event.key - pygame.K_1

pygame.quit()