# ==============================================================================
# Ejercicio 1: Factorial
# ==============================================================================

"""
1) Función recursiva que calcula el factorial de un número.
   Luego muestra los factoriales desde 1 hasta el número ingresado por el usuario.
"""

def factorial(num):
    if num == 0:  # Caso base: 0! = 1
        return 1
    else:  # Caso recursivo: n! = n * (n-1)!
        return num * factorial(num - 1)

NumeroEntero = int(input("Ingrese un número positivo para ver los factoriales: "))
print("\n=== Factoriales ===")
for cont in range(1, NumeroEntero + 1):
    print(f"{cont}! = {factorial(cont)}")

# ==============================================================================
# Ejercicio 2: Fibonacci
# ==============================================================================

"""
2) Función recursiva que calcula el número de Fibonacci en una posición dada.
   Luego muestra la serie completa hasta esa posición.
"""

def fibonacci(n):
    if n == 0:
        return 0  # Primer número de la serie
    elif n == 1:
        return 1  # Segundo número de la serie
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Suma de los dos anteriores

NumeroEntero = int(input("\nIngrese una posición para la serie de Fibonacci: "))
print("\n=== Serie de Fibonacci ===")
for cont in range(0, NumeroEntero + 1):
    print(f"Fibonacci({cont}) = {fibonacci(cont)}")

# ==============================================================================
# Ejercicio 3: Potencia
# ==============================================================================

"""
3) Función recursiva para calcular la potencia de un número.
   Usa la fórmula: base^exponente = base * base^(exponente-1)
"""

def potencia(base, exponente):
    if exponente == 0:
        return 1  # Cualquier número a la 0 es 1
    else:
        return base * potencia(base, exponente - 1)

print("\n=== Potencia ===")
print("2^3 =", potencia(2, 3))

# ==============================================================================
# Ejercicio 4: Conversión a Binario
# ==============================================================================

"""
4) Convierte un número decimal a binario usando recursión.
   Se construye la cadena binaria desde el cociente hasta el resto.
"""

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print("\n=== Conversión a Binario ===")
print("Binario de 10:", decimal_a_binario(10))

# ==============================================================================
# Ejercicio 5: Palíndromo
# ==============================================================================

"""
5) Verifica si una palabra es un palíndromo (se lee igual al derecho y al revés).
   Compara los extremos y llama recursivamente con la subcadena central.
"""

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True  # Palabras vacías o de 1 letra siempre son palíndromos
    elif palabra[0] != palabra[-1]:
        return False  # Si las letras externas no coinciden, no es palíndromo
    else:
        return es_palindromo(palabra[1:-1])  # Repetimos con el centro

print("\n=== Palíndromo ===")
print("¿'reconocer' es palíndromo?", es_palindromo("reconocer"))

# ==============================================================================
# Ejercicio 6: Suma de Dígitos
# ==============================================================================

"""
6) Suma los dígitos de un número entero usando recursión.
   No se usan strings, solo operaciones matemáticas (% y //).
"""

def suma_digitos(n):
    if n < 10:
        return n  # Un solo dígito
    else:
        return (n % 10) + suma_digitos(n // 10)  # Último dígito + suma del resto

print("\n=== Suma de Dígitos ===")
print("Suma de dígitos de 1234:", suma_digitos(1234))

# ==============================================================================
# Ejercicio 7: Pirámide de Bloques
# ==============================================================================

"""
7) Suma total de bloques para una pirámide.
   Cada nivel tiene un bloque menos que el anterior, hasta llegar a 1.
"""

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print("\n=== Pirámide de Bloques ===")
print("Bloques necesarios para base de 4:", contar_bloques(4))

# ==============================================================================
# Ejercicio 8: Contar Dígitos
# ==============================================================================

"""
8) Cuenta cuántas veces aparece un dígito dentro de un número.
   Se trabaja solo con operaciones matemáticas.
"""

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        resto = numero // 10
        if ultimo == digito:
            return 1 + contar_digito(resto, digito)
        else:
            return contar_digito(resto, digito)

print("\n=== Contar Dígito ===")
print("Veces que aparece 2 en 12233421:", contar_digito(12233421, 2))
