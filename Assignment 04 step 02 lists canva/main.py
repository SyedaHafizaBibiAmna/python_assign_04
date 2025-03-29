import pygame
import time

pygame.init()

CANVA_WIDTH = 400
CANVE_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 182, 193)

screen = pygame.display.set_mode((CANVA_WIDTH, CANVE_HEIGHT))
pygame.display.set_caption("Erase Effect in Pygame")

# Create grid
grid = []
for row in range(0, CANVE_HEIGHT // CELL_SIZE):
    for column in range(0, CANVA_WIDTH // CELL_SIZE):
        rect = pygame.Rect(column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get mouse position
    mouse_X, mouse_Y = pygame.mouse.get_pos()
    eraser.center = (mouse_X, mouse_Y)  # Using center for better positioning
    
    # Erase cells that collide with eraser
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
    grid = new_grid
    
    # Drawing
    screen.fill(WHITE)
    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)
    pygame.draw.rect(screen, PINK, eraser)
    
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()