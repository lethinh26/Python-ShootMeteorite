def fire_bullet(game):
    from Character.bullet import Bullet
    new_bullet = Bullet(game)
    game.bullets.add(new_bullet)


def remove_bullet(game):
    for bullet in game.bullets.copy():
        if bullet.rect.bottom <= 0:
            game.bullets.remove(bullet)
