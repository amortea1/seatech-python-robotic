from controller import Robot, Motor, PositionSensor







class move(Robot):

    timestep = 64
    max_speed=65


    Front_left_wheel = robot.getDevice('front right wheel motor')
    Front_right_wheel= robot.getDevice('front left wheel motor')
    Rear_left_wheel = robot.getDevice('rear left wheel motor')
    Rear_right_wheel = robot.getDevice('rear right wheel motor')

    Front_left_wheel.setPosition(float('inf'))
    Front_left_wheel.setVelocity(0.0)

    Front_right_wheel.setPosition(float('inf'))
    Front_right_wheel.setVelocity(0.0)

    Rear_left_wheel.setPosition(float('inf'))
    Rear_left_wheel.setVelocity(0.0)

    Rear_right_wheel.setPosition(float('inf'))
    Rear_right_wheel.setVelocity(0.0)


    def Front():
        Front_left_speed= 1.5*max_speed
        Front_right_speed = 1.5*max_speed
        Rear_left_speed = 1.5*max_speed
        Rear_right_speed = 1.5*max_speed


        Front_left_wheel.setVelocity(Front_left_speed)
        Front_right_wheel.setVelocity(Front_right_speed)
        Rear_left_wheel.setVelocity(Rear_left_speed)
        Rear_right_wheel.setVelocity(Rear_right_speed)

    def Right():
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
        Rear_right_wheel.setVelocity(Rear_right_speed)