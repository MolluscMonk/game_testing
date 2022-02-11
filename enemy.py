import pygame
import random

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




# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/Bullet.png").convert()
        self.size = self.surf.get_size()
        self.surf = pygame.transform.scale(self.surf, (int(self.size[0]/5), int(self.size[1]/5)))
        self.surf.set_colorkey((135, 206, 250), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(pygame.display.Info().current_w + 20, pygame.display.Info().current_w + 100),
                random.randint(0, pygame.display.Info().current_h),
            )
        )
        # self.speed = random.randint(5, 20)
        self.speed = random.randint(5, 15)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()