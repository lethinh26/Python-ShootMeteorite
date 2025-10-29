import pygame


class Settings:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.PLAYER_IMAGE = 0
        self.PLAYER_SPEED = 10
        self.PLAYER_SIZE = 0
        self.PLAYER_BULLET_SPEED = 0
        self.ENEMY_IMAGE =0
        self.ENEMY_SIZE = 0
        self.ENEMY_SPEED = 10
        self.ENEMY_BULLET_SPEED = 5
        self.ENEMY_SPAWN_RATE = 700
        self.BG_COLOR = 0
        self.TEXT_COLOR = 0
        self.SCORE = 0
        self.FONT = pygame.font.SysFont('Arial', 30)

    def updateScore(self, number):
        self.SCORE += number