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

        # bullet meteors
        self.bullets = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()

        # # self.ship = pygame.display.set_mode((int(self.settings.WIDTH), int(self.settings.HEIGHT)))
        # self.clock = pygame.time.Clock()
        # self.score = self.settings.FONT.render(f'score: {self.settings.SCORE}',True,(255,255,255))

        # pygame.display.is_fullscreen(True)
        self.clock = pygame.time.Clock()
        self.score = self.settings.SCORE

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

    def bullet_fire_collide_meteor(self):
        for meteorr in self.meteors.copy():
            for bulletr in self.bullets.copy():
                if meteorr.rect.colliderect(bulletr.rect):
                    self.bullets.remove(bulletr)
                    self.meteors.remove(meteorr)
                    self.score += 1
                    print(f'{self.score}')
        pass

    def meteor_collide_ship(self, waiting):
        for meteor in self.meteors.copy():
            if meteor.rect.colliderect(self.ship.rect):
                # exit
                waiting = False
                print('exit')

        # self.screen.fill((0,0,0, 0.6))

        return waiting



    
    def run_game(self):
        waiting = True
        running = True

        while running:

            self.font = self.settings.FONT.render(f'score: {self.score}', True, (255, 255, 255))
            waiting = self.meteor_collide_ship(waiting)
            moveShipEvent(self)
            self.bullet_fire_collide_meteor()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fire_bullet()

            self.screen.fill(self.settings.BG_COLOR)

            self.ship.blitme()

            self.bullets.update()
            for b in self.bullets.sprites():
                b.draw_bullet()

            self.update_meteors()
            self.draw_meteors()

            # create meteor
            self.create_meteor()

            self.screen.blit(self.font, (0,0))

            self.clock.tick(60)
            if waiting:
                print(waiting)
                pygame.display.flip()
            else:
                running = False

            # else:
                # self.font = self.settings.FONT.render(f"game over: {self.score}", True, (255, 255, 255))
                # self.screen.fill((0,0,0))
                # pygame.display.flip()

            # remove bullet coppy
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.BG_COLOR)

            pygame.display.flip()
        print('end game')

if __name__ == "__main__":
    game = ShootMeteorite()
    game.run_game()