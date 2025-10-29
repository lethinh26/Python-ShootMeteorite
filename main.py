import sys
import pygame
from Character import bullet
from Settings import config
from Character.ship import Ship
from event.shipEvent import moveShipEvent

from Character.bullet import Bullet
from Character.meteor import Meteor
import time

class ShootMeteorite:
    def __init__(self):
        pygame.init()
        self.settings = config.Settings()
        
        self.screen = pygame.display.set_mode((int(self.settings.WIDTH), int(self.settings.HEIGHT)))
        pygame.display.set_caption("Bắn thiên thạch")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()

        # self.ship = pygame.display.set_mode((int(self.settings.WIDTH), int(self.settings.HEIGHT)))
        self.clock = pygame.time.Clock()
        self.score = self.settings.FONT.render(f'score: {self.settings.SCORE}',True,(255,255,255))

        # pygame.display.is_fullscreen(True)
        self.clock = pygame.time.Clock()
        self.score = self.settings.FONT.render(f'score: {self.settings.SCORE}',True,(255,255,255))

        self.last_meteor_spawn_time = time.time()

    def fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def can_spawn_meteor(self):
        current_time = time.time()
        return (current_time - self.last_meteor_spawn_time) >= self.settings.ENEMY_SPAWN_RATE

    def create_meteor(self):
        if self.can_spawn_meteor():
            new_meteor = Meteor(self)
            self.meteors.add(new_meteor)
            self.last_meteor_spawn_time = time.time()

    def update_meteors(self):
        self.meteors.update()

    def draw_meteors(self):
        for meteor in self.meteors.sprites():
            meteor.blitme()

    def on_key_down(self, event):
        if event.key == pygame.K_SPACE:
            self.fire_bullet()
    
    def run_game(self):
        while True:

            # move ship
            moveShipEvent(self)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # if event.type == pygame.KEYDOWN:

            self.screen.fill((38, 13, 120))
            self.ship.blitme()
            self.screen.blit(self.score, (0,0))
            self.clock.tick(60)
            pygame.display.flip()

if __name__ == "__main__":
    game = ShootMeteorite()
    game.run_game()