import sys
import pygame
from Settings import config
from Character.ship import Ship

class ShootMeteorite:
    def __init__(self):
        pygame.init()
        self.settings = config.Settings()
        
        self.screen = pygame.display.set_mode((int(self.settings.WIDTH), int(self.settings.HEIGHT)))
        pygame.display.set_caption("Bắn thiên thạch")
        
        self.ship = Ship(self)
        # self.ship = pygame.display.set_mode((int(self.settings.WIDTH), int(self.settings.HEIGHT)))
        


        # pygame.display.is_fullscreen(True)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                self.screen.fill((38, 13, 120))
                self.ship.blitme()
                
                pygame.display.flip()


if __name__ == "__main__":
    game = ShootMeteorite()
    game.run_game()