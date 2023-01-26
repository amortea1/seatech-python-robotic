from controller import DistanceSensor

DISTANCE_SENSIOR_SAMPLING_PERIOD = 10

class EpuckDistanceSensor(DistanceSensor):
    def __init__(self, name):
        DistanceSensor.__init__(self, name)
        self.enable(DISTANCE_SENSIOR_SAMPLING_PERIOD)

class EpuckDistanceSensors():
    DISTANCE_THRESHOLD = 78

    def __init__(self):
        self.__front_left = EpuckDistanceSensor('front left distance sensor')
        self.__front_left2 = EpuckDistanceSensor('front right distance sensor')
        self.__front_right = EpuckDistanceSensor('rear left distance sensor')
        self.__front_right2 = EpuckDistanceSensor('rear right distance sensor')
    
    # Useful to debug Robot adventures
    def __str__(self):
        return "Left sensors: %s, %s\nRight sensors: %s, %s"%(
                self.__front_left.getValue(),
                self.__front_left2.getValue(),
                self.__front_right.getValue(),
                self.__front_right2.getValue()
        )

    def __repr__(self):
        return self.__str__()

    def front_left_collision_detected(self):
        return (self.__front_left.getValue() > self.DISTANCE_THRESHOLD or
                self.__front_left2.getValue() > self.DISTANCE_THRESHOLD)
    
    def front_right_collision_detected(self):
        return (self.__front_right.getValue() > self.DISTANCE_THRESHOLD or
                self.__front_right2.getValue() > self.DISTANCE_THRESHOLD)