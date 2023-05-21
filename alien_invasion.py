import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height =self.screen.get_rect().height
        #self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #self.bg_color = (230,230,230)
    def _check_keydown_events(event)
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(event)
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        #绘制所要求的平面
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #返回机制
        pygame.display.flip()#对屏幕进行隐藏
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
