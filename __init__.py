from engine.Engine import *
from menu.StartMenu import *
from engine.SplitAnimation import *
from engine.FrameContainer import *

def main():
    width = 600
    height = 500
    name = "myGame"

    # 框架图层容器
    frameContainer = FrameContainer()

    # 初始化engine和screen
    engine = Engine(ScreenDictionary.SCREEN_WIDTH,ScreenDictionary.SCREEN_HEIGHT,ScreenDictionary.SCREEN_NAME,
                    frameContainer)
    screen = engine.createScreen()

    # 测试firstFrame
    backGround = pygame.image.load(FileDictionary.MENU_BACKGROUD)
    backGround = pygame.transform.smoothscale(backGround, (100, 100))
    test = SplitAnimation(screen, backGround, 100, 100, 100, 100)

    frameContainer.appendFirstFrame(test)

    engine.setBackground(FileDictionary.MENU_BACKGROUD)

    engine.start()
    pass

if __name__ == '__main__':
    main()