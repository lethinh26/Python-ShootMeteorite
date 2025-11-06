import sys
import pygame
import time
from Settings import config
from Character.ship import Ship
from event.shipEvent import moveShipEvent
from event.gameEvent import handle_input_events
from event.bulletEvent import remove_bullet
from event.meteorEvent import update_meteors, draw_meteors, spawn_meteors_if_needed
from event.collisionEvent import bullet_collide_meteor, meteor_collide_ship
from event.uiEvent import update_score_display, show_start_screen, show_game_over_screen, draw_score

class ShootMeteorite:
    def __init__(self):
        pygame.init()
        self.settings = config.Settings()
        
        self.screen = pygame.display.set_mode((int(self.settings.WIDTH), int(self.settings.HEIGHT)))
        pygame.display.set_caption("Bắn thiên thạch")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()

        self.clock = pygame.time.Clock()
        
        self.last_meteor_spawn_time = time.time()
        
        # START, PLAYING, GAME_OVER
        self.game_state = "START"
        
        self.score_text = None
        update_score_display(self)

    def run_game(self):
        running = True

        while running:
            running = handle_input_events(self)
            if not running:
                break

            if self.game_state == "START":
                show_start_screen(self)
                
            elif self.game_state == "PLAYING":
                moveShipEvent(self)
                
                bullet_collide_meteor(self)
                
                if meteor_collide_ship(self):
                    self.game_state = "GAME_OVER"
                
                self.bullets.update()
                update_meteors(self)
                
                remove_bullet(self)
                
                spawn_meteors_if_needed(self)
                
                self.screen.fill(self.settings.BG_COLOR)
                self.ship.blitme()
                
                for i in self.bullets.sprites():
                    i.draw_bullet()
                
                draw_meteors(self)
                draw_score(self)
                
            elif self.game_state == "GAME_OVER":
                self.screen.fill(self.settings.BG_COLOR)
                self.ship.blitme()
                
                for i in self.bullets.sprites():
                    i.draw_bullet()
                
                draw_meteors(self)
                show_game_over_screen(self)

            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    game = ShootMeteorite()
    game.run_game()