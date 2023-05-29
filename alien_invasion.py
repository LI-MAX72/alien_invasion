import sys
import pygame
from settings import Settings
from ship import Ship
from Bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        #self.bg_color = (230,230,230)
    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height  = alien.rect.size
        #alien_width = alien.rect.width
        alien.x=alien_width+2*alien_width*alien_number
        alien.y=alien.rect.height+2*alien.rect.height*row_number
        alien.rect.y=alien.y
        alien.rect.x=alien.x
        self.aliens.add(alien)
    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height  = alien.rect.size
        #alien_width = alien.rect.width
        available_space_x = self.settings.screen_width-(2*alien_width)
        number_alien_x = available_space_x//(2*alien_width)
        #计算外星人的行数
        ship_height = self.ship.rect.height
        available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
        number_alien_row = available_space_y//(2*alien_height)

        for row_number in range(number_alien_row):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number,row_number)

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
        self.aliens.draw(self.screen)
        #返回机制
        pygame.display.flip()#对屏幕进行隐藏
    def _update_bulltes(self):
        for bullte in self.bulltes.copy():
            if bullte.rect.bottom <= 0:
                self.bulltes.remove(bullte)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        collisions  =pygame.sprite.groupcollide(self.bulltes,self.aliens,True,True)
        if not self.aliens:
            self.bulltes.empty()
            self._create_fleet()
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bulltes.update()
            self._update_bulltes()
            #print(len(self.bulltes))
            self._update_screen()
            self._update_aliens()
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
