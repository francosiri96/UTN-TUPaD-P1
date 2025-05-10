print("--------------------------------------------------")
print("Punto 1")
print("--------------------------------------------------")
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.
ListaNueva = list(range(1,100,4))
print(ListaNueva)

print("\n--------------------------------------------------")
print("Punto 2")
print("--------------------------------------------------")
# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

Lista2 = ["estudiantes", "edlp", 7, 0, "leon"]
print(Lista2[3])
print(Lista2[-2])

print("\n--------------------------------------------------")
print("Punto 3")
print("--------------------------------------------------")
# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
lista_vacia = []
lista_vacia.append("Dale leon")  # Agrega el primer elemento
lista_vacia.append("Estudio")    # Agrega el segundo elemento
lista_vacia.append("pincha")     # Agrega el tercer elemento
print(lista_vacia)              # Imprime la lista completa

print("\n--------------------------------------------------")
print("Punto 4")
print("--------------------------------------------------")
# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]

animales.remove("pez") # Como remover
animales.append("oso") # Como agregar ultimo
animales[1] = "loro"  # Como modificar 

print(animales)

print("\n--------------------------------------------------")
print("Punto 5")
print("--------------------------------------------------")
# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

print("En el programo lo que se muestra es una lista con numeros enteros. Se busca eliminar el numero mas grande con max y muestra la lista sin el numero")

print("\n--------------------------------------------------")
print("Punto 6")
print("--------------------------------------------------")
# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

lista6 =  list(range(10,35,5))

print(lista6[0],lista6[1])

print("\n--------------------------------------------------")
print("Punto 7")
print("--------------------------------------------------")
# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "Jeep"
autos[2]= "Peugueot"

print(autos)

print("\n--------------------------------------------------")
print("Punto 8")
print("--------------------------------------------------")
# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)


print("\n--------------------------------------------------")
print("Punto 9")
print("--------------------------------------------------")
# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

print("\n--------------------------------------------------")
print("Punto 10")
print("--------------------------------------------------")
# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla


lista_anidada = [[0],[True],[25.5,57.9,30.6],[False]]

print(lista_anidada)