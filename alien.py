import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.settings=ai_game.settings
        self.screen = ai_game.screen
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()
        #生成位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #精确的水平位置
        self.x = float(self.rect.x)
    def update(self):
        """"向右移动"""
        self.x +=self.settings.alien_speed
        self.rect.x=self.x
