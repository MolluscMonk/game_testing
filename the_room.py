
import pygame
import random
from player import Plane
from enemy import Enemy

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    FULLSCREEN,
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


pygame.init()

class iso:

    def x(self, x, y) -> int:


# isoX = cartX - cartY;
# isoY = (cartX + cartY) / 2;

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# player = Plane()




running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # pygame.draw.rect(surface=screen, color=(0, 0, 255), width=25, rect=75)
    pygame.draw.rect(screen,BLUE,(395,350,100,100))  # screen=surface, (x, y, height, width)
    pygame.draw.polygon(screen, BLACK, [[100, 150], [0, 200], [100, 250], [200, 200]], 3)

    # draws upside down T    
    pygame.draw.rect(screen,BLUE,(395,0,10,10))
    pygame.draw.rect(screen,BLUE,(385,10,10,10))
    pygame.draw.rect(screen,BLUE,(395,10,10,10))
    pygame.draw.rect(screen,BLUE,(405,10,10,10))

    # Flip the display
    pygame.display.flip()
    
pygame.quit()