#!/usr/bin/python

class SplitAnimation():
    '''分片的动画实体类，SplitAnimation包括x,y,width,height属性'''
    def __init__(self,screen,animation,wordX,wordY,width,height):
        self.wordX = wordX
        self.wordY = wordY
        self.screen = screen
        self.width = width
        self.height = height
        self.animation = animation
        self.objectX = 0
        self.objectY = 0

        #移动与旋转定义
        # 世界坐标移动
        self.endWordPosition = (self.wordY,self.wordY)
        self.endWordTime = 0

        pass

    def setSelfPosition(self,objectX,objectY):
        self.objectX = objectX
        self.objectY = objectY
        pass

    # 设置世界坐标位置
    def setWordPosition(self,wordX,wordY):
        self.wordX = wordX
        self.wordY = wordY
        pass

    def setAnimation(self):
        '''设置animation动画'''
        # 调用世界移动，世界旋转，自身移动，自身旋转的方法
        self.__setWordNextPositon()
        self.screen.blit(self.animation,(self.wordX + self.objectX ,self.wordY + self.objectY))


    def wordMove(self,endPosition,time):
        '''设置世界坐标终点位置以及从当前位置移动到终点位置的时间
            如果 endWordTime != 0 ，说明此时正在移动，因此此次输入无效
            因此只有当endWordTime == 0 时才设置
        '''
        if self.endWordTime == 0:
            self.endWordPosition = endPosition
            self.endWordTime = time
        pass

    # 世界坐标重终点设置
    def __setWordNextPositon(self):

        # 这里需要考虑由于取int导致的位置偏移情况
        if self.endWordTime > 0 :
            self.wordX = (self.endWordPosition[0] - self.wordX) / self.endWordTime + self.wordX
            self.wordY = (self.endWordPosition[1] - self.wordY) / self.endWordTime + self.wordY
            # 每调用一次，endWordTime -1,直到endWordTime为0
            self.endWordTime = self.endWordTime - 1
        else:
            self.wordX = self.endWordPosition[0]
            self.wordY = self.endWordPosition[1]
        pass

        pass

    def __dirrectObjectMove(self,endPosition):
        '''物体坐标系移动'''
        pass

    def __wordRotate(self,routateCenter,angle):
        '''以世界坐标系旋转'''

        pass

    def objectRotate(self, routateCenter, angle):
        '''以自身坐标系旋转'''

        pass

    
    pass