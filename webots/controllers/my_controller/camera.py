from controller import Camera
from controller import RangeFinder
from controller import Robot, Motor, PositionSensor


CAMERA_SAMPLING_PERIOD = 50
DISTANCE_SENSIOR_SAMPLING_PERIOD = 50

class Camera1(Camera):
    def __init__(self):
        super().__init__('camera rgb')
        self.enable(CAMERA_SAMPLING_PERIOD)
    
    def getValue(self):
        #print(self.__array) """

        #""" self.getImage() """
        #""" self.getImageArray() """
        self.getImage()
        return self.getImageArray()

class Camera2(RangeFinder):
    def __init__(self):
        super().__init__('camera depth')
        self.enable(CAMERA_SAMPLING_PERIOD)
        self.__minrange=self.getMinRange()
        self.__maxrenge=self.getMaxRange()
        self.__minwith=self.getWidth()
        self.__minheight=self.getHeight()
        
    def is_on_edge(self):
        view = self.getImageArray()
        on_edge = False
        print(view)
        for pix in view:
            pass

        # traitement ... on_edge = True/False
        
        return on_edge
        print(self.__minrange)
        print(self.__maxrenge)
        print(self.__minwith)
        print(self.__minheight)
