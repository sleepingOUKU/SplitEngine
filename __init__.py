from engine.Engine import *
from animation.SplitAnimation import *
from engine.FrameContainer import *
from config.EngineConfig import *
from comons.FileDictionary import *

def main():

    # 框架图层容器
    frameContainer = FrameContainer()

    # 初始化engine和screen
    engine = Engine(EngineConfig.SCREEN_WIDTH,EngineConfig.SCREEN_HEIGHT,EngineConfig.SCREEN_NAME,
                    frameContainer)
    screen = engine.createScreen()

    # 测试firstFrame
    backGround = pygame.image.load(FileDictionary.MENU_BACKGROUD)
    backGround = pygame.transform.smoothscale(backGround, (100, 100))
    test = SplitAnimation(screen, backGround, 100, 100, 100, 100)
    test.wordMove((200,200),20)
    frameContainer.appendFirstFrame(test)

    # 设置背景图片
    engine.setBackground(FileDictionary.MENU_BACKGROUD)

    # 引擎渲染启动
    engine.start()
    pass

if __name__ == '__main__':
    main()