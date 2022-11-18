import time
from client import RobotClient
from inverse_kinematics import position_to_dof
import numpy as np


# Conectarse al robot

r = RobotClient(address="192.168.0.15")  # Recuerda usar una dirección válida
r.connect()

def move_robot_to_xyz(robot, x, y, z):
    q0, q1, q2 = position_to_dof(x, y, z)
    robot.set_joints(q0, q1, q2)

r.set_joints(0,0,100)