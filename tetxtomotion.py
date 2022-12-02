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
    robot.set_joints(-23, 0, 105)
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

def dosos(robot):
    robot.set_joints(-40, 0, 136)
    time.sleep(0.5)
    robot.set_joints(-40, 38, 136)
    time.sleep(0.5)
    robot.home()

def resos(robot):
    robot.set_joints(-32, 0, 136)
    time.sleep(0.5)
    robot.set_joints(-32, 38, 136)
    time.sleep(0.5)
    robot.home()

def fasos(robot):
    robot.set_joints(-11, 0, 136)
    time.sleep(0.5)
    robot.set_joints(-11, 38, 136)
    time.sleep(0.5)
    robot.home()

def solsos(robot):
    robot.set_joints(-5, 0, 136)
    time.sleep(0.5)
    robot.set_joints(-5, 38, 136)
    time.sleep(0.5)
    robot.home()

def lasos(robot):
    robot.set_joints(5, 0, 136)
    time.sleep(0.5)
    robot.set_joints(5, 38, 136)
    time.sleep(0.5)
    robot.home()

def dodosos(robot):
    robot.set_joints(26, 0, 136)
    time.sleep(0.5)
    robot.set_joints(26, 38, 136)
    time.sleep(0.5)
    robot.home()

def reresos(robot):
    robot.set_joints(35, 0, 136)
    time.sleep(0.5)
    robot.set_joints(35, 38, 136)
    time.sleep(0.5)
    robot.home()


def textomotion(robot,string):

    a=string.lower().split(" ")

    if a[0] == "do" or a[0]=="2" or a[0]=="no":
            do(robot)
    elif a[0] == "re":
           re(robot)
    elif a[0] == "mi":
            mi(robot)
    elif a[0] == "fa" or a[0]=="pa":
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
    elif a[0] == "mini" or a[0]=="mimi":
            mimi(robot)
    elif a[0] == "jaja":
            fafa(robot)
    elif a[0] == "estrellita":
        do(robot)
        do(robot)
        sol(robot)
        sol(robot)
        la(robot)
        la(robot)
        sol(robot)
        time.sleep(0.5)
        fa(robot)
        fa(robot)
        mi(robot)
        mi(robot)
        re(robot)
        re(robot)
        do(robot)

