import sys
import pygame
from settings import Settings
from ship import Ship
from Bullet import Bullet
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
        self.bulltes = pygame.sprite.Group()
        #self.bg_color = (230,230,230)
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullte()
    def _fire_bullte(self):
        if len(self.bulltes) < self.settings.bullet_allowed:
            new_bullte = Bullet(self)
            self.bulltes.add(new_bullte)
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _check_events(self):
        #网上相关的解决方案
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        #绘制所要求的平面
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullte in self.bulltes.sprites():
            bullte.draw_bullet()
        #返回机制
        pygame.display.flip()#对屏幕进行隐藏
    def _update_bulltes(self):
        for bullte in self.bulltes.copy():
            if bullte.rect.bottom <= 0:
                self.bulltes.remove(bullte)
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bulltes.update()
            self._update_bulltes()
            #print(len(self.bulltes))
            self._update_screen()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
