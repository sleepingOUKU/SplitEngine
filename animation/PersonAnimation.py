from animation.SplitAnimation import *

class PersonAnimation(SplitAnimation):

    def move(self,endPositon,time):
        if time > 0 :
            subX = (self.x - endPositon[0]) / time
            subY = (self.y - endPositon[1]) / time

        else:
            self.x = endPositon[0]
            self.y = endPositon[1]
            self.setAnimation()
        pass


        pass

    pass