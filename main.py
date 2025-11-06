import sys
import pygame
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

        self.clock = pygame.time.Clock()
        
        self.last_meteor_spawn_time = time.time()
        
        # START, PLAYING, GAME_OVER
        self.game_state = "START"
        
        self.score_text = None
        self.update_score()



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

    def update_score(self):
        self.score_text = self.settings.FONT.render(f'Score: {self.settings.SCORE}', True, (255, 255, 255))

    def bullet_fire_collide_meteor(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.meteors, True, True)
        if collisions:
            self.settings.updateScore(len(collisions))
            self.update_score()

    def meteor_collide_ship(self):
        for meteor in self.meteors.sprites():
            if meteor.rect.colliderect(self.ship.rect):
                return True
        return False



    def reset_game(self):
        self.bullets.empty()
        self.meteors.empty()
        self.settings.SCORE = 0
        self.update_score()
        self.ship.rect.x = self.settings.WIDTH / 2
        self.ship.rect.y = self.settings.HEIGHT -60
        self.last_meteor_spawn_time = time.time()
        self.game_state = "PLAYING"

    def show_start_screen(self):
        self.screen.fill((20, 10, 60))
        
        title_font = pygame.font.SysFont('Arial', 60, bold=True)
        des_font = pygame.font.SysFont('Arial', 30)
        
        title = title_font.render('Shoot Meteorite', True, (255,215,0))
        des = des_font.render('Press E to start', True, (255,255,255))
        
        title_rect = title.get_rect(center=(self.settings.WIDTH/2, self.settings.HEIGHT/3))
        des_rect = des.get_rect(center=(self.settings.WIDTH/2, self.settings.HEIGHT/2))

        self.screen.blit(title, title_rect)
        self.screen.blit(des, des_rect)

    def show_game_over_screen(self):
        overlay = pygame.Surface((self.settings.WIDTH, self.settings.HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        self.screen.blit(overlay, (0, 0))
        
        game_over_font = pygame.font.SysFont('Arial', 70, bold=True)
        score_font = pygame.font.SysFont('Arial', 40)
        des_font = pygame.font.SysFont('Arial', 30)
        
        game_over_text = game_over_font.render('GAME OVER', True, (255, 50, 50))
        final_score = score_font.render(f'Score: {self.settings.SCORE}', True, (255, 215, 0))
        restart_text = des_font.render('Press R to restart', True, (255, 255, 255))
        
        game_over_rect = game_over_text.get_rect(center=(self.settings.WIDTH/2, self.settings.HEIGHT/3))
        score_rect = final_score.get_rect(center=(self.settings.WIDTH/2, self.settings.HEIGHT/2))
        restart_rect = restart_text.get_rect(center=(self.settings.WIDTH/2, self.settings.HEIGHT/2 +70))
        
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(final_score, score_rect)
        self.screen.blit(restart_text, restart_rect)

    def run_game(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if self.game_state == "START" and event.key == pygame.K_e:
                        self.reset_game()
                    
                    elif self.game_state == "GAME_OVER":
                        if event.key == pygame.K_r:
                            self.reset_game()
                        elif event.key == pygame.K_ESCAPE:
                            running = False
                    
                    elif self.game_state == "PLAYING" and event.key == pygame.K_SPACE:
                        self.fire_bullet()

            if self.game_state == "START":
                self.show_start_screen()
                
            elif self.game_state == "PLAYING":
                moveShipEvent(self)
                
                self.bullet_fire_collide_meteor()
                
                if self.meteor_collide_ship():
                    self.game_state = "GAME_OVER"
                
                self.bullets.update()
                self.update_meteors()
                
                for bullet in self.bullets.copy():
                    if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)
                
                if len(self.meteors) < self.settings.MAX_ENEMIES:
                    self.create_meteor()
                
                self.screen.fill(self.settings.BG_COLOR)
                self.ship.blitme()
                
                for b in self.bullets.sprites():
                    b.draw_bullet()
                
                self.draw_meteors()
                self.screen.blit(self.score_text, (10, 10))
                
            elif self.game_state == "GAME_OVER":
                self.screen.fill(self.settings.BG_COLOR)
                self.ship.blitme()
                
                for b in self.bullets.sprites():
                    b.draw_bullet()
                
                self.draw_meteors()
                self.show_game_over_screen()

            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    game = ShootMeteorite()
    game.run_game()