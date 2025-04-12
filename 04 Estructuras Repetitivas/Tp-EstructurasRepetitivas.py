""""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

Cont = -1
for cont in range(-1,100):
    cont += 1
    print (cont)

"""""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
print("///////////////////////////////////////////")
NumeroEntero = int(input("Ingrese un numero y le dire la cantidad de digitos!!"))
cantidad_de_numeros = len(str(abs(NumeroEntero)))

print ("La cantidad de digitos que tiene el numero es ", cantidad_de_numeros)


""""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

print("///////////////////////////////////////////")
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

inicio = min(numero1, numero2) + 1
fin = max(numero1, numero2)

suma = 0

for i in range(inicio, fin):
    suma += i

print("La suma de los números entre", numero1, "y", numero2, "es:", suma)



""""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

print("///////////////////////////////////////////")

total = 0
numero = int(input("Ingresá un número (0 para terminar): "))
while numero != 0:
    total += numero
    numero = int(input("Ingresá un número (0 para terminar): "))

print("La suma total es:", total)
""""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

"""
print("///////////////////////////////////////////")

import random

numero_aleatorio = random.randint(0, 9)  # Número aleatorio entre 0 y 9
intentos = 1  # El primer intento es al menos uno

numero_usuario = int(input("Adivina un número entre 0 y 9: "))

while numero_usuario != numero_aleatorio:
    intentos += 1  # Aumentamos el contador de intentos
    numero_usuario = int(input("Adivina un número entre 0 y 9: "))

print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")



""""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.

"""
print("///////////////////////////////////////////")

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


""""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
print("///////////////////////////////////////////")

limite = int(input("Ingresá un número entero positivo: "))
suma = 0

for i in range(limite + 1):
    suma += i

print("La suma de todos los números entre 0 y", limite, "es:", suma)


""""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
print("///////////////////////////////////////////")

cantidad = 5
impares = 0
pares = 0 
positivos = 0 
negativos = 0 

for i in range(cantidad):
    num = int(input(f"Ingresá el número {i+1}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

""""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

print("///////////////////////////////////////////") 

cantidad = 5  


suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingresá el número {i + 1}: "))
    suma += numero


media = suma / cantidad
print("La media de los números ingresados es:", media)


""""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = input("Ingresá un número: ")
numero_invertido = numero[::-1]
print("Número invertido:", numero_invertido)