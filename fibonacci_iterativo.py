# Fibonacci Iterativo.
def fibonacci_iterativo(numero):
    if numero == 0:  # caso base
        return 0
    elif numero == 1: # caso base
        return 1
    varA = 0
    varB = 1
    for i in range(2, numero + 1):
        varA, varB = varB, varA + varB
    return varB
numero = 50
resultado = fibonacci_iterativo(numero)
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")