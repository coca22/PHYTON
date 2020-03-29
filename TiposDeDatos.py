#numero 01
print("Ejercicio Numero 01: ")
def secuencia():

    num1=0
    total = 1
    while num1 != 1:
        num1 = int(input("Ingrese el numero: "))
        total = total * num1

    print("Su resultado es: " + str(total))


secuencia()

#numero 02
print("Ejercicio Numero 02: ")
lista = []
cantidad=int (input("Con cuantos numeros trabajara: "))
i=1
total=1
while(cantidad > 0):
    numero = int(input("Numero #" + str(i) + ":  "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1
    total = total * numero
#no pude ingresar el F :(

print("Lista: ", lista)
print(total)

#numero 03
print("Ejercicio Numero 03: ")
lista = []
cantidad=int (input("Con cuantos numeros trabajara: "))
mayor=0
i=1

while(cantidad > 0):
    numero = int(input("Numero: " + str(i) + ":  "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1


mayor = max(lista)

print("Lista: ", lista)
print("Mayor: ", mayor)

#numero 04
def fibonacci(contador,n,p1,p2):
 var = ""
 if(contador!=n):
  var=fibonacci(contador+1,n,p2,p1+p2)
  var=str(p2)+" "+var
 return var
n = int(input("Ingrese el numero a trabajar: "))
if(n>0):
 a=fibonacci(0,(n-1),0,1)
 print ("0 "+a)




#numero 06
print("Ejercicio Numero 06: ")
import math
num = input("Ingrese el numero a trabajar: ")
x = int(num)
factorial = math.factorial(x)
print("El factorial es: " , factorial)
