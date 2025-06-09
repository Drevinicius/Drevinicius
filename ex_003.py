"""Verificar se o número é ímpar ou par"""

numero = 7

# Entrada do usuário
"""numero = int(input("Digite um valor: "))"""

if numero % 2 == 0: # Se o resto da divisão/ módulo é 0 então ele é par
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar") # Saída se número for 7