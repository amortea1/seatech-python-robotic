from controller import Robot, Motor, PositionSensor



from camera import Camera1




class move(Robot):



    def __init__(self):
        super().__init__()
        camera=Camera1()
        self.imestep = 64
        self.max_speed=6

        self.Front_left_wheel = self.getDevice('front right wheel motor')
        self.Front_right_wheel= self.getDevice('front left wheel motor')
        self.Rear_left_wheel = self.getDevice('rear left wheel motor')
        self.Rear_right_wheel = self.getDevice('rear right wheel motor')

        self.Front_left_wheel.setPosition(float('inf'))
        self.Front_left_wheel.setVelocity(0.0)

        self.Front_right_wheel.setPosition(float('inf'))
        self.Front_right_wheel.setVelocity(0.0)

        self.Rear_left_wheel.setPosition(float('inf'))
        self.Rear_left_wheel.setVelocity(0.0)

        self.Rear_right_wheel.setPosition(float('inf'))
        self.Rear_right_wheel.setVelocity(0.0)

        

        

    def Front(self):
        self.Front_left_speed= 1.5*self.max_speed
        self.Front_right_speed = 1.5*self.max_speed
        self.Rear_left_speed = 1.5*self.max_speed
        self.Rear_right_speed = 1.5*self.max_speed


        self.Front_left_wheel.setVelocity(self.Front_left_speed)
        self.Front_right_wheel.setVelocity(self.Front_right_speed)
        self.Rear_left_wheel.setVelocity(self.Rear_left_speed)
        self.Rear_right_wheel.setVelocity(self.Rear_right_speed)

    def forward(self):
        """Go forward"""
        self.Front()

    def backward(self):
        """Go backward"""

    def run(self):
        self.forward()


    """ ef Right():
        Front_left_speed= 1.5*max_speed
        Front_right_speed = -1.5*max_speed
        Rear_left_speed = -1.5*max_speed
        Rear_right_speed = 1.5*max_speed


        Front_left_wheel.setVelocity(Front_left_speed)
        Front_right_wheel.setVelocity(Front_right_speed)
        Rear_left_wheel.setVelocity(Rear_left_speed)
        Rear_right_wheel.setVelocity(Rear_right_speed)

    def Left():
        Front_left_speed= -1.5*max_speed
        Front_right_speed = 1.5*max_speed
        Rear_left_speed = 1.5*max_speed
        Rear_right_speed =-1.5*max_speed


        Front_left_wheel.setVelocity(Front_left_speed)
        Front_right_wheel.setVelocity(Front_right_speed)
        Rear_left_wheel.setVelocity(Rear_left_speed)
        Rear_right_wheel.setVelocity(Rear_right_speed) """