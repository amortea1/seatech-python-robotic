from controller import Camera
from controller import Robot, Motor, PositionSensor


CAMERA_SAMPLING_PERIOD = 50
DISTANCE_SENSIOR_SAMPLING_PERIOD = 50

class Camera1(Camera):
    def __init__(self):
        super().__init__('camera rgb')
        self.enable(CAMERA_SAMPLING_PERIOD)