# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
# Programación 1
# Trabajo Práctico N.º 6: Estructuras de Datos Complejas
# Nombre: Franco Siri

# --------------------------------------------
# 1) Añadir frutas al diccionario
# --------------------------------------------

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# --------------------------------------------
# 2) Actualizar precios de frutas
# --------------------------------------------

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# --------------------------------------------
# 3) Lista de frutas (sin precios)
# --------------------------------------------

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# --------------------------------------------
# 4) Agenda telefónica
# --------------------------------------------

agenda = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número telefónico: ")
    agenda[nombre] = telefono

consulta = input("Ingrese el nombre del contacto a buscar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# --------------------------------------------
# 5) Frase: palabras únicas y conteo de apariciones
# --------------------------------------------

frase = input("Ingresá una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", conteo)

# --------------------------------------------
# 6) Promedio de notas de alumnos
# --------------------------------------------

alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1}: ")) for j in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio:.2f}")

# --------------------------------------------
# 7) Alumnos que aprobaron parciales
# --------------------------------------------

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 6, 7}

ambos = parcial1 & parcial2           # Aprobó ambos parciales
solo_uno = parcial1 ^ parcial2        # Aprobó solo uno
al_menos_uno = parcial1 | parcial2    # Aprobó al menos uno

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# --------------------------------------------
# 8) Stock de productos
# --------------------------------------------

stock = {'Yerba': 10, 'Azúcar': 5}

producto = input("Ingrese el nombre del producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("Cuántas unidades desea agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no existe. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# --------------------------------------------
# 9) Agenda de eventos con tuplas (día, hora)
# --------------------------------------------

agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '15:00'): 'Clase',
}

dia = input("Día: ")
hora = input("Hora: ")
evento = agenda_eventos.get((dia, hora), "No hay actividad programada.")
print("Actividad:", evento)

# --------------------------------------------
# 10) Invertir diccionario de países y capitales
# --------------------------------------------

paises = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Italia': 'Roma'
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)
