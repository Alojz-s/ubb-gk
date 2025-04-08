import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab2Z1")

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

circle_radius = 200
square_size = 200
center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, BLACK, center, circle_radius)

    square_rect = pygame.Rect(0, 0, square_size, square_size)
    square_rect.center = center
    pygame.draw.rect(screen, YELLOW, square_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
