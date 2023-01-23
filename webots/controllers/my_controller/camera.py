from controller import Camera
from controller import Robot, Motor, PositionSensor

CAMERA_SAMPLING_PERIOD = 50
CAMERA_RECOGNITION_SAMPLING_PERIOD = 100

class Camera1(Camera):
    def __init__(self):
        super().__init__('camera rgb')
        self.enable(CAMERA_SAMPLING_PERIOD)
        """ self.recognitionEnable(CAMERA_RECOGNITION_SAMPLING_PERIOD)
        self.__tracked_name = None

    def track_object(self, object_name):
        self.__tracked_name = object_name

    def is_tracked_object_present(self):
        objs = self.getRecognitionObjects()
        for obj in objs:
            print('I saw something !')
            print(obj)
            if self.__tracked_name == obj.get_model().decode("utf-8"):
                self.__recognized_object = obj
                return True
        return False """