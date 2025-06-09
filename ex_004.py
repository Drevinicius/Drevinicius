"""Quantos numeros na lista são pares"""

array = [1, 2, 3, 4, 5, 6]
contador = 0 # uma variavel auxiliar pra contar os valores pares

# Caso tenha uma entrada pelo usuário
"""
array = list()
for i in renge(0, 5):
    valor_do_usuario = int(input("Digite um valor para o array: "))
    
    if valor_do_usuario % 2 == 0:
        contador += 1
    
    array.append(valor_do_usuario)
"""

for valor in array:
    if valor % 2 == 0:
        contador += 1

print(f"A quantidade de numeros pares é {contador}")