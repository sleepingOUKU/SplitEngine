
class KeyEvent():

    _instance = None
    _keyEventDictionary = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)


        return cls._instance


    def listenKeyEvent(self):
        """
        监听key事件
        :return:
        """


        pass

    def addKeyListener(self):
        pass

    pass