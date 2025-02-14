import math

print ("Hola")
print ("Felipe Buitrago")
print ("A continuacion, mira la siguiente función: ")

#CALCULAR FIBONACCI
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


#FUNCION CLACULAR AREA CIRCULO
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

#FUNCION MATEMATICA CUADRADO 
def calcular_cuadrado(numero):
    """
    Calcula el cuadrado de un número.

    :param numero: El número que se desea elevar al cuadrado.
    :return: El cuadrado del número.
    """
    return numero ** 2

# Ejemplo de uso
numero = 4
cuadrado = calcular_cuadrado(numero)
print(f"El cuadrado de {numero} es: {cuadrado}")
