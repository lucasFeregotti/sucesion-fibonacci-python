import matplotlib.pyplot as plt
import time

def fibonacci_tabulacion(numero):
    if numero <= 1:
        return numero 
    tabla = [0] * (numero + 1) 
    tabla[0] = 0  # Los casos base
    tabla[1] = 1
    for i in range(2, numero + 1): 
        tabla[i] = tabla[i - 1] + tabla[i - 2]
    return tabla[numero]

# Definir el rango de números para los cuales se medirá el tiempo
numeros = range(1, 40)
tiempos = []

# Medir el tiempo de ejecución
for numero in numeros:
    start_time = time.time()
    fibonacci_tabulacion(numero)
    end_time = time.time()
    tiempos.append(end_time - start_time)

plt.figure(figsize=(10, 6), facecolor='white')  # Cambia el color que prefieras
plt.plot(numeros, tiempos, marker='o', linestyle='-', color='b')  # crea el gráfico de líneas, conecta los puntos definidos por las coordenadas en los ejes X e Y.
plt.xlabel('Número de Fibonacci')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Tiempo de Ejecución del Cálculo de Fibonacci (Tabulacion)')
plt.grid(True)
plt.show()