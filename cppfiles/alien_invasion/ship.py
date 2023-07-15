import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):

        self.screeen =ai_game.screen
        self.screeen_rect =ai_game.screen.get_rect()
          # 加载飞船图像 获取外接矩形
        self.image =pygame.image.load('images/ship.bmp')
        self.rect =self.image.get_rect()

        self.rect.midbottom = self.screeen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screeen.blit(self.image,self.rect)