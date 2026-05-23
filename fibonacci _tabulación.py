# Fibonacci con Tabulación.
def fibonacci_tabulacion(numero):
    if numero <= 1:
        return numero 
    tabla = [0] * (numero + 1) 
    tabla[0] = 0  # Los casos base
    tabla[1] = 1
    for i in range(2, numero + 1): 
        tabla[i] = tabla[i - 1] + tabla[i - 2]
    return tabla[numero]
numero = 50
resultado = fibonacci_tabulacion(numero)
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")