#!/usr/bin/python
import pygame

class Engine:
    def __init__(self,width,height,name,frameContainer):
        self.width = width
        self.height = height
        self.name = name

        # 将框架渲染分为6层，第一层为背景图层，第二层为环境物体图层，第三层为animation层，第四层为animation遮蔽层，第五层为环境物体层，第六层为整体环境层
        self.frameContainer = frameContainer

        pygame.init()
        pass

    def createScreen(self):
        # 创建screen
        self.screen = pygame.display.set_mode((self.width,self.height),0,32)
        pygame.display.set_caption(self.name)

        return self.screen
        pass


    # 设置menu背景
    def setBackground(self,backGroudPic):
        backGround = pygame.image.load(backGroudPic)
        backGround = pygame.transform.smoothscale(backGround,(self.width,self.height))
        self.screen.blit(backGround,(0,0))
        pass

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # 接收到退出事件后退出程序
                    exit()
            self.surfaceAllFrame()
            pygame.display.update()
        pass


    # 渲染所有的页面，从第一层到第六层
    def surfaceAllFrame(self):

        for splitAnimation in self.frameContainer.getFirstFrame() :
            self.surfaceFrame(splitAnimation)
            pass;

        for splitAnimation in self.frameContainer.getSecondFrame() :
            self.surfaceFrame(splitAnimation)
            pass;

        for splitAnimation in self.frameContainer.getThirdFrame() :
            self.surfaceFrame(splitAnimation)
            pass;

        for splitAnimation in self.frameContainer.getSixthFrame() :
            self.surfaceFrame(splitAnimation)
            pass;

        for splitAnimation in self.frameContainer.getFifthFrame() :
            self.surfaceFrame(splitAnimation)
            pass;

        for splitAnimation in self.frameContainer.getSixthFrame() :
            self.surfaceFrame(splitAnimation)
            pass;
        pass


    def surfaceFrame(self,splitAnimation):
        #渲染动画，通过setAnimation方法
        splitAnimation.setAnimation()
        pass

    pass