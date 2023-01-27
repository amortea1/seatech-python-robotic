
from controller import Lidar

class Lidar_Controller():
    def __init__(self, robot) -> None:
        self. timestep = int(robot.getBasicTimeStep())
        self.front_lidar =robot.getDevice('lidar')
        self.front_lidar.enable(self.timestep)
        self.front_lidar.enablePointCloud()
        