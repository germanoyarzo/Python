
def imprimirTateti(tateti):
    for fila in tateti:
        for i in range(len(fila)):#i es cada elemento
            if i==len(fila)-1:
                print(fila[i], end='\n')
            else:
                print(fila[i], end='  ')

tateti = [
    ['|', '  ','|', '|', '  ','|','|', '  ','|'],
    ['|', '  ','|', '|', '  ','|','|', '  ','|'],
    ['|', '  ','|', '|', '  ','|','|', '  ','|']
]




def cambiarTablero(tateti, posicion, jugador):
    if jugador:#es verdadero
        simbolo='x'
    else:
        simbolo='o'
    
    if posicion==1:
        if tateti [3][1]=='  ':
            tateti[3][1]= simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion==2:
        if tateti[3][4]=='  ':
            tateti[3][4]=simbolo
            return 0
        else: 
            return 'Esa posicion ya esta ocupada.'
    elif posicion==3:
        if tateti[3][7]=='  ':
            tateti[3][7]=simbolo
            return 0
        else: 
            return 'Esa posicion ya esta ocupada.'
    elif posicion==4:
        if tateti[2][1]=='  ':
            tateti[2][1]=simbolo
            return 0
        else: 
            return 'Esa posicion ya esta ocupada.'
    elif posicion==5:
        if tateti[2][4]=='  ':
            tateti[2][4]=simbolo
            return 0
        else: 
            return 'Esa posicion ya esta ocupada.'
    elif posicion==6:
        if tateti[2][7]=='  ':
            tateti[2][7]=simbolo
            return 0
        else: 
            return 'Esa posicion ya esta ocupada.'
    elif posicion==7:
        if tateti[1][1]=='  ':
            tateti[1][1]=simbolo
            return 0
        else: 
            return 'Esa posicion ya esta ocupada.'
    elif posicion==8:
        if tateti[1][4]=='  ':
            tateti[1][4]=simbolo
            return 0
        else: 
            return 'Esa posicion ya esta ocupada.'
    elif posicion==9:
        if tateti[1][7]=='  ':
            tateti[1][7]=simbolo
            return 0
        else: 
            return 'Esa posicion ya esta ocupada.'

def ganador(tateti):
    for simbolo in ['x', 'o']:
        fila1=tateti[1][1]== simbolo and tateti[1][4]== simbolo and tateti[1][7]==simbolo
        fila2=tateti[2][1]== simbolo and tateti[2][4]== simbolo and tateti[2][7]==simbolo
        fila3=tateti[3][1]== simbolo and tateti[3][4]== simbolo and tateti[3][7]==simbolo
        columna1=tateti[1][1]== simbolo and tateti[1][4]== simbolo and tateti[1][7]==simbolo
        columna2=tateti[2][1]== simbolo and tateti[2][4]== simbolo and tateti[2][7]==simbolo
        columna3=tateti[3][1]== simbolo and tateti[3][4]== simbolo and tateti[3][7]==simbolo
        diagonalAbajo=tateti[1][1]== simbolo and tateti[2][4]== simbolo and tateti[3][7]==simbolo
        diagonalArriba=tateti[3][1]== simbolo and tateti[2][4]== simbolo and tateti[3][7]==simbolo
    if fila1 or fila2 or fila3 or columna1 or columna2 or columna3 or diagonalAbajo or diagonalArriba:
        if simbolo== 'x':
            return 1
        elif simbolo=='o':
            return 2
        

turno1=True 

turno=0

# respuesta=input("Que simbolo desea elegir? 'X' u 'O' ")
# respuesta=respuesta.upper()
# if respuesta=="x":
jugador1=input("jugador 1 ingrese su nombre : ") 
jugador2=input("jugador 2 ingrese su nombre: ")   
while turno < 9: 
    if turno1:

        print("jugador 1: elegi una posicion")
    else:
        
        print("jugador 2: elegi una posicion")
        
    jugada=int(input())

    valor=cambiarTablero(tateti, jugada, turno1)
    if valor==0:
         #salio todo bien
        turno1=not turno1
        turno1+=1
        imprimirTateti(tateti)
        if ganador(tateti)==1:
            print("jugador1 ha ganado!!")
            break
        elif ganador(tateti)==2:
            print("jugador2 ha ganado!!") 
            break   
    else:
        print(valor)
    if turno==9:
        print("Empate")
        



