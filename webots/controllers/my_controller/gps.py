from controller import GPS
from controller import Robot, Motor, PositionSensor

# def stop(self):
        

class Gps_controller(GPS):
    def __init__(self,name, timestep) -> None:
        super().__init__(name)
        self.enable(int(timestep))
        

    @property
    def position(self):
        return self.getValues()

    # @property
    # def coordinate_system(self) -> int:
    #     return self.gps.getCoordinateSystem()

    def getCoordinates(self):
        return self.getValues()

    # @staticmethod
    # def convertToDegreesMinutesSeconds(decimalDegree):
