import pygame
import time


def handle_input_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
            
        if event.type == pygame.KEYDOWN:
            if game.game_state == "START" and event.key == pygame.K_e:
                reset_game(game)
            elif game.game_state == "GAME_OVER":
                if event.key == pygame.K_r:
                    reset_game(game)
                elif event.key == pygame.K_ESCAPE:
                    return False
            elif game.game_state == "PLAYING" and event.key == pygame.K_SPACE:
                from event.bulletEvent import fire_bullet
                fire_bullet(game)
    
    return True


def reset_game(game):
    game.bullets.empty()
    game.meteors.empty()
    game.settings.SCORE = 0
    from event.uiEvent import update_score_display
    update_score_display(game)
    game.ship.rect.x = game.settings.WIDTH /2
    game.ship.rect.y = game.settings.HEIGHT -60
    game.last_meteor_spawn_time = time.time()
    game.game_state = "PLAYING"
