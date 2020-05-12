#!/usr/bin/python
from comons.LightEnum import LightEnum

class BaseLight():

    def __init__(self):

        # 设置默认光源未
        self.type = LightEnum.DIRECTIONAL_LIGHT


        pass

    def on(self):
        pass

    def off(self):
        pass

    def setColor(self,color):
        pass

    # 渲染光照
    def surfaceLight(self):

        pass

    pass