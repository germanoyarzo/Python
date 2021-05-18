
import random
from random import choice


def randomDados():
	dado1=random.choice([1,2,3,4,5,6])
	print("DADO 1: ", dado1)
	dado2=random.choice([1,2,3,4,5,6])
	print("DADO 2: ", dado2)
	suma=dado1+dado2
	return suma
print("La suma de los dados es: ",randomDados())

respuesta=input("Desea tirar los dados nuevamente? s(si)/n(no) ")
while respuesta=="s": #upper si lo ingresa en mayuscula no cambia en nada
	print("La suma de los dados es: ",randomDados())
	respuesta=input("Desea tirar los dados nuevamente? s(si)/n(no) ")


		







