#!/usr/bin/python

class SplitAnimation():
    '''分片的动画实体类，SplitAnimation包括x,y,width,height属性'''
    def __init__(self,screen,animation,x,y,width,height):
        self.x = x
        self.y = y
        self.screen = screen
        self.width = width
        self.height = height
        self.animation = animation
        pass

    def setAnimation(self):
        '''设置animation动画'''
        self.screen.blit(self.animation,(self.x,self.y))

    def start(self):

        pass

    pass