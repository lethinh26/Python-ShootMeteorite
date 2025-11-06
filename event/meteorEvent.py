import time


def can_spawn_meteor(game):
    current_time = time.time()
    return (current_time - game.last_meteor_spawn_time) >= game.settings.ENEMY_SPAWN_RATE


def create_meteor(game):
    if can_spawn_meteor(game):
        from Character.meteor import Meteor
        new_meteor = Meteor(game)
        game.meteors.add(new_meteor)
        game.last_meteor_spawn_time = time.time()


def update_meteors(game):
    game.meteors.update()


def draw_meteors(game):
    for meteor in game.meteors.sprites():
        meteor.blitme()


def spawn_meteors_if_needed(game):
    if len(game.meteors) < game.settings.MAX_ENEMIES:
        create_meteor(game)
