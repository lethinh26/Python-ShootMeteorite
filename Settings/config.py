import pygame


class Settings:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600

        self.PLAYER_IMAGE = "assests/spaceship.png"
        self.PLAYER_SPEED = 5
        self.PLAYER_SIZE = 0
        self.PLAYER_BULLET_SPEED = 5

        self.ENEMY_IMAGE = "assests/meteor.png"
        self.ENEMY_SIZE = 0
        self.ENEMY_SPEED = 10
        self.ENEMY_SPAWN_RATE = 0.5

        self.BULLET_WIDTH = 5
        self.BULLET_HEIGHT = 10
        self.BULLET_COLOR = "#e8b651"

        self.BG_COLOR = (38, 13, 120)
        self.TEXT_COLOR = 0
        self.SCORE = 0
        self.FONT = pygame.font.SysFont('Arial', 30)

    def updateScore(self, number):
        self.SCORE += number