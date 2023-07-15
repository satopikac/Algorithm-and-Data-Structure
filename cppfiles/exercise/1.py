# 创建一个背景为蓝色的pygame窗口
import sys #使用其中工具退出游戏

import pygame

class Game:
    def __init__(self):
        pygame.init() # 初始化背景设置
        self.screen = pygame.display.set_mode((1920,1080)) #设置窗口
        self.bg_color = (0,104,120) #设置背景色
        pygame.display.set_caption("一个练习窗口") #设置标题

    def run_game(self):
        #游戏主循环
        while True:
          
          for event in pygame.event.get() : #监视事件
              if event.type == pygame.QUIT:  #按x就结束程序
                  sys.exit()

          self.screen.fill(self.bg_color) #绘制屏幕
          pygame.display.flip() #最近绘制的屏幕可见

    
# 创建实例 
my_exercise=Game()
my_exercise.run_game()
