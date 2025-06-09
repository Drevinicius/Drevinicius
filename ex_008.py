"""Somando intervalo de numeros N"""

def soma (numero):
    contador = 0
    for valor in range(1, numero+1):
        contador += valor
    return contador

print(f"Soma: {soma(5)}") # Saída: 15