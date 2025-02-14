import math

print ("Hola")
print ("Felipe Buitrago")
print ("A continuacion, mira la siguiente función: ")

def calcular_fibonacci(n):
    """
    Calcula la secuencia de Fibonacci hasta el enésimo número.

    :param n: La cantidad de números en la secuencia de Fibonacci.
    :return: Una lista con la secuencia de Fibonacci.
    """
    secuencia = [0, 1]
    while len(secuencia) < n:
        siguiente_valor = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente_valor)
    return secuencia[:n]

# Ejemplo de uso
n = 10
resultado = calcular_fibonacci(n)
print(f"Secuencia de Fibonacci hasta el {n}º número: {resultado}")

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: El radio del círculo.
    :return: El área del círculo.
    """
    area = math.pi * (radio ** 2)
    return area

# Ejemplo de uso
radio = 5
area = calcular_area_circulo(radio)
print(f"El área de un círculo con radio {radio} es: {area}")

print ("Adios")