import sys
import pygame
from Settings import config
from Character.ship import Ship
from event.shipEvent import moveShipEvent


class ShootMeteorite:
    def __init__(self):
        pygame.init()
        self.settings = config.Settings()
        
        self.screen = pygame.display.set_mode((int(self.settings.WIDTH), int(self.settings.HEIGHT)))
        pygame.display.set_caption("Bắn thiên thạch")

        self.ship = Ship(self)
        # self.ship = pygame.display.set_mode((int(self.settings.WIDTH), int(self.settings.HEIGHT)))
        self.clock = pygame.time.Clock()
        self.score = self.settings.FONT.render(f'score: {self.settings.SCORE}',True,(255,255,255))

        # pygame.display.is_fullscreen(True)

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