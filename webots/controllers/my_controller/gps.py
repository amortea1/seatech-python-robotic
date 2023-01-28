from controller import GPS


class Gps_controller():
    def __init__(self,robot) -> None:
        self.gps =robot.getDevice('gps')
        self.gps.enable(int(robot.getBasicTimeStep()))
    @property
    def position(self):
        return self.gps.getValues()

    # def getCoordinates(self):
    #     return self.gps.getValues()
        
    # def checkGPS(self):
            
    #     border={
    #             "left":-3.5,
    #             "right":3.5,
    #             "front":3.5,
    #             "back":-3.5
    #     }
    #     limit=0.3

    #     Coordinates=self.getValues()
    #     long=[]
    #     test=False
    #     for key,value in border.items():
    #         long.append(abs(Coordinates[0]-border[key]))
    #         long.append(abs(Coordinates[1]-border[key]))
            
    #     longs = min(long)
    #     if(longs<limit):
    #         print(True)
    #         return True
    #     else:
    #         print(False)
    #         return False