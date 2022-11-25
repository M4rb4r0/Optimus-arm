
def textomotion(string):

    a=string.lower().split()

    for i in range(len(a)-1):
        if a[i] == "do":

        elif a[i] == "re":

        elif a[i] == "mi":

        elif a[i] == "fa":

        elif a[i] == "sol":

        elif a[i] == "la":

        elif a[i] == "si":

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


