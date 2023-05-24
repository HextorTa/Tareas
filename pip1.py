#cachipun
import random
A=0
B=0

def Cachipun(A,B):
    if A==B:
        print("Empate")
    elif (A==1 and B==2) or (A==2 and B==3) or (A==3 and B==1):
        print("Jugador Gana")
    else:
        print("Jugador Pierde")
def Trans(A):
    if A=="PIEDRA":
        A=1
    elif A=="TIJERA":
        A=2
    else:
        A=3

A=input("ingrese su eleccion/PIEDRA/PAPEL/TIJERA/: ")
B=random.randint(1,3)
Trans(A)
Cachipun(A,B)
