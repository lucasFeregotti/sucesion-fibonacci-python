#Fibonacci recursivo.
def fibonacci_recursivo(numero):
    if numero <= 1:
        return numero
    else:
        return fibonacci_recursivo(numero - 1) + fibonacci_recursivo(numero - 2)
numero = 50
resultado = fibonacci_recursivo(numero)
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")