#!/usr/bin/python
from comons.LightEnum import LightEnum

class BaseLight():

    def __init__(self):

        # 设置默认光源为DirectionLight
        self.type = LightEnum.DIRECTIONAL_LIGHT
        self.status = LightEnum.LIGHT_STATUS_ON

        pass

    def on(self):
        self.status = LightEnum.LIGHT_STATUS_ON
        pass

    def off(self):
        self.status = LightEnum.LIGHT_STATUS_OFF
        pass

    def setColor(self,color):
        pass

    # 渲染光照
    def surfaceLight(self):

        # 当status为启动时进行渲染
        if self.status :

            pass
        pass

    pass