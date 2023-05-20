import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        #self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #self.bg_color = (230,230,230)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #绘制所要求的平面
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            #返回机制
            pygame.display.flip()#对屏幕进行隐藏

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
