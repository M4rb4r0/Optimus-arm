from escuchar import *
from tetxtomotion import *

#Creación de variable por voz
q=0
Text=escuchar(q)

#Conexión al robot
r = RobotClient(address="192.168.0.15")
r.connect()
#Reconocimiento de nota y movimiento
textomotion(r,Text)