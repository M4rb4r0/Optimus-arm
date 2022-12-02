from prueba import *

def do(robot):
    robot.set_joints(-33, 0, 90)
    time.sleep(0.5)
    robot.set_joints(-33, 55, 90)
    time.sleep(0.5)
    robot.home()

def re(robot):
    robot.set_joints(-27, 0, 105)
    time.sleep(0.5)
    robot.set_joints(-27, 49, 105)
    time.sleep(0.5)
    robot.home()

def mi(robot):
    robot.set_joints(-23, 40, 105)
    time.sleep(0.5)
    robot.set_joints(-23, 49, 105)
    time.sleep(0.5)
    robot.home()

def fa(robot):
    robot.set_joints(-16, 0, 105)
    time.sleep(0.5)
    robot.set_joints(-16, 49, 105)
    time.sleep(0.5)
    robot.home()

def sol(robot):
    robot.set_joints(-7, 0, 105)
    time.sleep(0.5)
    robot.set_joints(-7, 49, 105)
    time.sleep(0.5)
    robot.home()

def la(robot):
    robot.set_joints(0, 0, 105)
    time.sleep(0.5)
    robot.set_joints(0, 48, 105)
    time.sleep(0.5)
    robot.home()

def si(robot):
    robot.set_joints(8, 0, 105)
    time.sleep(0.5)
    robot.set_joints(8, 48, 105)
    time.sleep(0.5)
    robot.home()

def dodo(robot):
    robot.set_joints(13, 0, 105)
    time.sleep(0.5)
    robot.set_joints(13, 48, 105)
    time.sleep(0.5)
    robot.home()

def r(robot):
    robot.set_joints(22, 0, 105)
    time.sleep(0.5)
    robot.set_joints(22, 48, 105)
    time.sleep(0.5)
    robot.home()

def mimi(robot):
    robot.set_joints(30, 0, 105)
    time.sleep(0.5)
    robot.set_joints(30, 48, 105)
    time.sleep(0.5)
    robot.home()

def fafa(robot):
    robot.set_joints(36, 0, 105)
    time.sleep(0.5)
    robot.set_joints(36, 48, 105)
    time.sleep(0.5)
    robot.home()

def textomotion(robot,string):

    a=string.lower().split(" ")

    if a[0] == "do":
            do(robot)
    elif a[0] == "re":
           re(robot)
    elif a[0] == "mi":
            mi(robot)
    elif a[0] == "fa":
            fa(robot)
    elif a[0] == "sol":
           sol(robot)
    elif a[0] == "la":
            la(robot)
    elif a[0] == "sii":
           si(robot)
    elif a[0] == "dodo":
           dodo(robot)
    elif a[0] == "r":
           r(robot)
    elif a[0] == "mini":
            mimi(robot)
    elif a[0] == "jaja":
        fafa(robot)