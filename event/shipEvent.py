import pygame


def moveShipEvent(object) :
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        object.ship.update('left')
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        object.ship.update('right')
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        object.ship.update('up')
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        object.ship.update('down')