import pygame
import random
from pygame.sprite import Sprite

class Meteor(Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load(game.settings.ENEMY_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.settings.WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)  

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.ENEMY_SPEED
        self.rect.y = self.y

        if self.rect.top >= self.settings.HEIGHT:
            self.kill()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
