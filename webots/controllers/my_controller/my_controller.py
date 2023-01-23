"""my_controller controller."""
#include <math.h>
#include <stdio.h>
#include <webots/compass.h>
#include <webots/gps.h>
#include <webots/keyboard.h>
#include <webots/motor.h>
#include <webots/robot.h>
from move import move

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
#from controller import Robot, Motor, PositionSensor
#doit ajouter l'option Robot souligner

# create the Robot instance.
robot = move()

# get the time step of the current world.
#timestep = int(robot.getBasicTimeStep())


timestep = 64
max_speed=65


""" Front_left_wheel = robot.getDevice('front right wheel motor')
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

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep) """



# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    

    robot.Front()
    

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
