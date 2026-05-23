# Pruebas Empíricas
import time

def fibonacci_iterativo(numero):
    if numero == 0: 
        return 0
    elif numero == 1: 
        return 1
    varA = 0
    varB = 1
    for i in range(2, numero + 1):
        varA, varB = varB, varA + varB
    return varB

def fibonacci_recursivo(numero):
    if numero <= 1:
        return numero
    else:
        return fibonacci_recursivo(numero - 1) + fibonacci_recursivo(numero - 2)

def fibonacci_memo(numero, memo={}):
    if numero in memo:
        return memo[numero]
    if numero <= 1:  
        return numero
    memo[numero] = fibonacci_memo(numero - 1, memo) + fibonacci_memo(numero - 2, memo)
    return memo[numero]

def fibonacci_tabulacion(numero):
    if numero <= 1:
        return numero
    
    tabla = [0] * (numero + 1)   
    tabla[0] = 0  
    tabla[1] = 1
    for i in range(2, numero + 1):   
        tabla[i] = tabla[i - 1] + tabla[i - 2]
    
    return tabla[numero]

numero = 40
# Medir tiempo de fibonacci_iterativo
start_time = time.time()
print("\nFIBONACCI ITERATIVO:")
print(f"Tiempo de inicio: {start_time} segundos")
resultado = fibonacci_iterativo(numero)
end_time = time.time()
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")
print(f"Tiempo final: {end_time} segundos")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
print("----------------------------------------------------------\n")
# Medir tiempo de fibonacci_recursivo
start_time = time.time()
print("FIBONACCI RECURSIVO:")
print(f"Tiempo de inicio: {start_time} segundos")
resultado = fibonacci_recursivo(numero)
end_time = time.time()
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")
print(f"Tiempo final: {end_time} segundos")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
print("----------------------------------------------------------\n")
# Medir tiempo de fibonacci_memo'start_time = time.time()
print("FIBONACCI CON MEMORIZACION:")
print(f"Tiempo de inicio: {start_time} segundos")
resultado = fibonacci_memo(numero)
end_time = time.time()
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")
print(f"Tiempo final: {end_time} segundos")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
print("----------------------------------------------------------\n")
# Medir tiempo de fibonacci_tabulacion
start_time = time.time()
print("FIBONACCI CON TABULACION:")
print(f"Tiempo de inicio: {start_time} segundos")
resultado = fibonacci_tabulacion(numero)
end_time = time.time()
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")
print(f"Tiempo final: {end_time} segundos")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
print("----------------------------------------------------------\n")