# Fibonacci con Memorización.
def fibonacci_memo(numero, memo={}):
    if numero in memo:
        return memo[numero]
    if numero <= 1:  # caso base
        return numero
    memo[numero] = fibonacci_memo(numero - 1, memo) + fibonacci_memo(numero - 2, memo)
    return memo[numero]
numero = 50
resultado = fibonacci_memo(numero)
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")