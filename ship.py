import pygame

class Ship:
    def __init__(self,ai_game):
        #初始化以及赋予初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #加载飞机图像和外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        #新飞机放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """if self.moving_right:
            self.x += self.settings.ship_speed
        elif self.moving_left:
            self.x += self.settings.ship_speed"""
        #优化：
        if self.moving_right and self.rect.x < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed
        #转化小数和整数
        self.rect.x = self.x
    def blitme(self):
        '''指定位置绘制飞机'''
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
