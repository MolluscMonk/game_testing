import pygame


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

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # super(Player, self).__init__()
        super().__init__()
        self.surf = pygame.image.load("images/plane.png").convert()
        self.size = self.surf.get_size()
        self.surf = pygame.transform.scale(self.surf, (int(self.size[0]/5), int(self.size[1]/5)))
        self.surf.set_colorkey((135, 206, 250), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > pygame.display.Info().current_w:
            self.rect.right = pygame.display.Info().current_w
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= pygame.display.Info().current_h:
            self.rect.bottom = pygame.display.Info().current_h