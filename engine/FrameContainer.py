#!/usr/bin/python
class FrameContainer():
    # 容器，用于包含层级frame

    def __init__(self):
        self.firstFrame = []
        self.secondFrame = []
        self.thirdFrame = []
        self.fourthFrame = []
        self.fifthFrame = []
        self.sixthFrame = []
        pass

    def appendFirstFrame(self,splitAnimation):
        self.firstFrame.append(splitAnimation)
        pass
    def appendSecondFrame(self,splitAnimation):
        self.secondFrame.append(splitAnimation)
        pass
    def appendThirdFrame(self,splitAnimation):
        self.thirdFrame.append(splitAnimation)
        pass
    def appendFourthFrame(self,splitAnimation):
        self.fourthFrame.append(splitAnimation)
        pass
    def appendFifthFrame(self,splitAnimation):
        self.fifthFrame.append(splitAnimation)
        pass
    def appendSixthFrame(self,splitAnimation):
        self.sixthFrame.append(splitAnimation)
        pass

    def getFirstFrame(self):
        return self.firstFrame
        pass
    def getFirstFrame(self):
        return self.firstFrame
        pass
    def getSecondFrame(self):
        return self.secondFrame
        pass
    def getThirdFrame(self):
        return self.thirdFrame
        pass
    def getFifthFrame(self):
        return self.fifthFrame
        pass
    def getSixthFrame(self):
        return self.sixthFrame
        pass

    pass