#FUNCIONES 

import math


def imprimir_hola_mundo():
    print("Hola Mundo")

def saludar_usuario(nombre):
    print (f"Hola {nombre}")

def informacion_personal(nombre,edad,apellido,residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

def calcular_area_circulo(radio):
    print(f"{math.pi * radio **2 }" )

def calcular_perimetro_circulo(radio):
   print(f"{2 * math.pi * radio}")

def segundos_a_horas(segundos):
    horas = segundos/3600
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (no se puede dividir por cero)"
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def calcular_promedio(a, b, c):
    return (a + b + c) / 3



#Programa principals

imprimir_hola_mundo()       #tarea 1 hMUNDO


nombre = input("Como se llama? ")        # tarea 2 saudar
saludar_usuario(nombre)

edad = input("Que edad tiene? ")
apellido = input("Como es su apellido? ")
residencia = input("Donde vive? ")

informacion_personal(nombre, edad, apellido, residencia)    # tarea 3


radio = float(input("Ingrese el tamaño del radio "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)                             # tarea 4


segundos = int(input("indique cuantos segundos "))

segundos_a_horas(segundos)                              # tarea 5

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)                                  # tarea 6


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)             #tarea7 

# Mostrar resultados de forma clara
print(f"\nResultados de las operaciones entre {a} y {b}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#8 
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")


#9 


celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
#10 

promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {promedio:.2f}")