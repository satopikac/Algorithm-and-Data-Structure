# 创建表示游戏的类，创建空的pygame窗口
import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏创建游戏资源"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

      

    def run_game(self):
        """开启游戏主循环"""

        while True:
            self._check_events()
            self._update_screen()
            
    
    def _check_events(self):
        """响应按键与鼠标事件"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                          self.ship.rect.x +=1
    
    def _update_screen(self):
         """更新屏幕图像，切换新屏幕"""
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()
         pygame.display.flip()






         

if __name__ == '__main__':
    ai =AlienInvasion()
    ai.run_game()