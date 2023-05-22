import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()
        #生成位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #精确的水平位置
        self.x = float(self.rect.x)
