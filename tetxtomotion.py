from prueba import *
def textomotion(robot,string):

    a=string.lower().split()

    for i in range(len(a)-1):
        if a[i] == "do":
            move_robot_to_xyz(robot, -27, 0, 90)
            time.sleep(0.5)
            move_robot_to_xyz(robot, -27, 36, 90)

        elif a[i] == "re":
            move_robot_to_xyz(robot, -21, 0, 105)
            move_robot_to_xyz(robot, -21, 26, 105)

        elif a[i] == "mi":
            move_robot_to_xyz(robot, -16, 0, 105)
            move_robot_to_xyz(robot, -16, 26, 105)

        elif a[i] == "fa":
            move_robot_to_xyz(robot, -11, 0, 105)
            move_robot_to_xyz(robot, -11, 26, 105)

        elif a[i] == "sol":
            move_robot_to_xyz(robot, -7, 0, 105)
            move_robot_to_xyz(robot, -7, 26, 105)

        elif a[i] == "la":
            move_robot_to_xyz(robot, -0, 0, 105)
            move_robot_to_xyz(robot, -0, 26, 105)

        elif a[i] == "si":
            move_robot_to_xyz(robot, 8, 0, 105)
            move_robot_to_xyz(robot, 0, 26, 105)

# más de una nota a la vez
def textomotion2(string,lista_movimientos):

    a = string.lower().split()
    for i in range(len(a)-1):
            if a[i]==None:
                for e in range(len(lista_movimientos-1)):

                    if lista_movimientos[e] is None:

                        return None
                    
                    if lista_movimientos[e] == "do":

                        textomotion2(a,lista_movimientos[e:])

                    if lista_movimientos[e] == "re":

                        textomotion2(a,lista_movimientos[e:])

                    if lista_movimientos[e] == "mi":

                        textomotion2(a,lista_movimientos[e:])

                    if lista_movimientos[e] == "fa":

                        textomotion2(a,lista_movimientos[e:])

                    if lista_movimientos[e] == "sol":

                        textomotion2(a,lista_movimientos[e:])

                    if lista_movimientos[e] == "la":

                        textomotion2(a,lista_movimientos[e:])

                    if lista_movimientos[e] == "si":

                        textomotion2(a,lista_movimientos[e:])

            if a[i] == "do":
                lista_movimientos.append(a[i])
                textomotion2(a[i:],lista_movimientos)

            if a[i] == "re":
                lista_movimientos.append(a[i])
                textomotion2(a[i:],lista_movimientos)

            if a[i] == "mi":
                lista_movimientos.append(a[i])
                textomotion2(a[i:],lista_movimientos)

            if a[i] == "fa":
                lista_movimientos.append(a[i])
                textomotion2(a[i:],lista_movimientos)

            if a[i] == "sol":
                lista_movimientos.append(a[i])
                textomotion2(a[i:],lista_movimientos)

            if a[i] == "la":
                lista_movimientos.append(a[i])
                textomotion2(a[i:],lista_movimientos)

            if a[i] == "si":
                lista_movimientos.append(a[i])
                textomotion2(a[i:],lista_movimientos)


