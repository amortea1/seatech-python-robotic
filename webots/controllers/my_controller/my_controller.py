"""my_controller controller."""
#include <math.h>
#include <stdio.h>
#include <webots/compass.h>
#include <webots/gps.h>
#include <webots/keyboard.h>
#include <webots/motor.h>
#include <webots/robot.h>


# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, PositionSensor
#doit ajouter l'option Robot souligner

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
#timestep = int(robot.getBasicTimeStep())
timestep = 64


Front_left_wheel = robot.getMotor('front right wheel motor')
Front_right_wheel= robot.getMotor('front left wheel motor')
Rear_left_wheel = robot.getMotor('rear left wheel motor')
Rear_right_wheel = robot.getMotor('rear right wheel motor')

Front_left_wheel.setPosition(float('inf'))
Front_left_wheel.setVelocity(0.0)

Front_right_wheel.setPosition(float('inf'))
Front_right_wheel.setVelocity(0.0)

Rear_left_wheel.setPosition(float('inf'))
Rear_left_wheel.setVelocity(0.0)

Rear_right_wheel.setPosition(float('inf'))
Rear_right_wheel.setVelocity(0.0)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    #left_speed= 0.5*max_speed
    #right_speed = 0.5*max_speed

    #left_motor.setVelocity(left_speed)
    #right_motor.setVelocity(left_speed)

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
