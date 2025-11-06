import pygame
class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.speed = game.settings.PLAYER_SPEED

        self.image = pygame.image.load(game.settings.PLAYER_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = game.settings.WIDTH / 2
        self.rect.y = game.settings.HEIGHT - 60

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, direction: str):
        if direction == 'left':
            if self.rect.left > 0:
                self.rect.x -= self.speed
        if direction == 'right':
            if self.rect.right < self.settings.WIDTH:
                self.rect.x += self.speed
        if direction == 'down':
            if self.rect.bottom < self.settings.HEIGHT:
                self.rect.y += self.speed
        if direction == 'up':
            if self.rect.top > 0:
                self.rect.y -= self.speed

