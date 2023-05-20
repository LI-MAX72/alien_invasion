import pygame
class Ship:
    def __init__(self,ai_game):
        #初始化以及赋予初始位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #加载飞机图像和外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        #新飞机放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        '''指定位置绘制飞机'''
        self.screen.bilt(self.image,self.rect)
