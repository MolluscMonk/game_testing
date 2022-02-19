
import math
import pygame
import random
# from player import Plane
# from enemy import Enemy

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


class Coords:
    # def __init__(self, x: float, y: float):
    #     self.r = math.sqrt(x**2 + y**2)
    #     self.theta = math.atan(y/x)
    
    def to_polar(self, x: float, y: float) -> tuple[float]:
        """
        returns radius, theta
        """
        return math.sqrt(x**2 + y**2), math.atan(y/x)

    def to_cart(self, r: float, t: float) -> tuple[float]:
        """
        returns x, y
        """
        return r*math.cos(t), r*math.sin(t)
    
def main():

    pygame.init()
    clock = pygame.time.Clock()
    class iso:



    # polar = Polar(10, 10)
    # print(polar.r)
    # print(polar.theta)
    coord = Coords()
    r, t = coord.to_polar(10, 10)
    print(r, t)
    x, y = coord.to_cart(r, t)
    print(x, y)



    #testing push
    # isoX = cartX - cartY;
    # isoY = (cartX + cartY) / 2;

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # player = Plane()

    radius = 200
    start_loc = [300, 300]
    steps = 4
    pi = math.pi

    circle = []
    # point = 
    for i in range(steps * 2 + 1):
        rad = (i/steps)*pi
        # print(f'{i}/{steps} PI')
        point = [math.cos(rad)*radius + start_loc[0], math.sin(rad)*radius + start_loc[1]]
        circle.append(point)


    # circle = rotate(circle)
    # for item in circle:
    #     print(item)
    
    game_loop(screen, circle, clock)


def game_loop(screen, circle, clock):
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
        pygame.draw.polygon(screen, BLACK, circle, 3)

        circle = rotate(circle)

        # draws upside down T    
        # pygame.draw.rect(screen,BLUE,(395,0,10,10))
        # pygame.draw.rect(screen,BLUE,(385,10,10,10))
        # pygame.draw.rect(screen,BLUE,(395,10,10,10))
        # pygame.draw.rect(screen,BLUE,(405,10,10,10))

        pygame.display.flip()
        clock.tick(0.1)
    pygame.quit()


def rotate(circle: list) -> list:

    coord = Coords()
    # consider changing the 0,0 of the graph
    for i, item in enumerate(circle):
        tmp = coord.to_polar(item[0], item[1])
        circle[i] = [tmp[0], tmp[1]]

    for i, item in enumerate(circle):
        circle[i] = [item[0], item[1] + math.pi/16]

    for i, item in enumerate(circle):
        tmp = coord.to_cart(item[0], item[1])
        circle[i] = [tmp[0], tmp[1]]


    return circle
    





if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)

        raise ex