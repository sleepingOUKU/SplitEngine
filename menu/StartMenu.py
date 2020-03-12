import pygame
from comons.ScreenDictionary import ScreenDictionary
from comons.FileDictionary import FileDictionary

class StartMenu:
    def __init__(self,screen):
        self.sceen = screen
        pass

    # 设置menu背景
    def setBackground(self):
        backGround = pygame.image.load(FileDictionary.MENU_BACKGROUD)
        backGround = pygame.transform.smoothscale(backGround,(ScreenDictionary.SCREEN_WIDTH,ScreenDictionary.SCREEN_HEIGHT))
        self.sceen.blit(backGround,(0,0))
        pass

    pass