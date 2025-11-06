import pygame


def update_score_display(game):
    game.score_text = game.settings.FONT.render(f'Score: {game.settings.SCORE}', True, (255, 255, 255))


def show_start_screen(game):
    game.screen.fill((20, 10, 60))
    
    title_font = pygame.font.SysFont('Arial', 60, bold=True)
    des_font = pygame.font.SysFont('Arial', 30)
    
    title = title_font.render('Shoot Meteorite', True, (255, 215, 0))
    des = des_font.render('Press E to start', True, (255, 255, 255))
    
    title_rect = title.get_rect(center=(game.settings.WIDTH / 2, game.settings.HEIGHT / 3))
    des_rect = des.get_rect(center=(game.settings.WIDTH / 2, game.settings.HEIGHT / 2))

    game.screen.blit(title, title_rect)
    game.screen.blit(des, des_rect)


def show_game_over_screen(game):
    overlay = pygame.Surface((game.settings.WIDTH, game.settings.HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    game.screen.blit(overlay, (0, 0))
    
    game_over_font = pygame.font.SysFont('Arial', 70, bold=True)
    score_font = pygame.font.SysFont('Arial', 40)
    des_font = pygame.font.SysFont('Arial', 30)
    
    game_over_text = game_over_font.render('GAME OVER', True, (255, 50, 50))
    final_score = score_font.render(f'Score: {game.settings.SCORE}', True, (255, 215, 0))
    restart_text = des_font.render('Press R to restart', True, (255, 255, 255))
    
    game_over_rect = game_over_text.get_rect(center=(game.settings.WIDTH / 2, game.settings.HEIGHT / 3))
    score_rect = final_score.get_rect(center=(game.settings.WIDTH / 2, game.settings.HEIGHT / 2))
    restart_rect = restart_text.get_rect(center=(game.settings.WIDTH / 2, game.settings.HEIGHT / 2 + 70))
    
    game.screen.blit(game_over_text, game_over_rect)
    game.screen.blit(final_score, score_rect)
    game.screen.blit(restart_text, restart_rect)


def draw_score(game):
    game.screen.blit(game.score_text, (10, 10))
