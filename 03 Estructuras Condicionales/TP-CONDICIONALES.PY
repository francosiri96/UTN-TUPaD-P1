"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
Edad = int(input("Que edad tiene?"))
MayorEDAD = 18
if Edad >= MayorEDAD:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""

Nota = int(input("Cual fue su nota en el parcial? "))
NotaAprobanda = 6
if Nota >= NotaAprobanda:
    print("Aprobado")
else: print("Desaprobado")

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""

Numero = int(input("Diga un numero "))
if Numero % 2 ==0:
    print("EL numero es par")
else: 
    print("El numero es impar")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""""

EdadActual = int(input("Que edad tiene usted? "))

if EdadActual < 12:
    print("Usted es un niño")
elif EdadActual >= 12 and EdadActual <18:
    print ("Usted es un Adolescente")
elif EdadActual >= 18 and EdadActual <30:
    print ("Usted es un Adulto/a joven")

elif EdadActual >=30 :
    print("Usted es adulyo")


"""""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""

contraseña = input("Escriba una contraseña que tenga entre 8 y 14 caracteres ")

resultado = len(contraseña)

if resultado >=8 and resultado <=14:
    print ("contraseña correcta ")
else: 
    print ("contraseña incorrecta verifique la cantidad de caracteres ")


""""6"""

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media= mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana > moda:
    print("📈 Hay sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("📉 Hay sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("🔔 Sin sesgo (distribución simétrica)")
else:
    print("🤔 No se puede determinar claramente un sesgo")


    """"7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""

frase = input("Ingresá una frase o palabra: ")

if frase[-1] in "aeiouAEIOU":
   print(frase + "!")
else:
   print(frase)


"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""
nombre = input("Escribí tu nombre: ")
opcion = input("Elegí una opción:\n1 - Mayúsculas\n2 - Minúsculas\n3 - Primera letra en mayúscula\nOpción: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")


"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

magnitud = float(input("Ingresá la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


""""10"""
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

fecha = mes * 100 + dia

if fecha >= 1221 or fecha <= 320:
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif 321 <= fecha <= 620:
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif 621 <= fecha <= 920:
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif 921 <= fecha <= 1220:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print("Estás en:", estacion)