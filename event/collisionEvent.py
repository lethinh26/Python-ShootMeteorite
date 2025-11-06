import pygame

def bullet_collide_meteor(game):
    collisions = pygame.sprite.groupcollide(game.bullets, game.meteors, True, True)
    if collisions:
        game.settings.updateScore(len(collisions))
        from event.uiEvent import update_score_display
        update_score_display(game)


def meteor_collide_ship(game):
    for meteor in game.meteors.sprites():
        if meteor.rect.colliderect(game.ship.rect):
            return True
    return False
