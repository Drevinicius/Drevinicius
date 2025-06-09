"""Dada uma lista de números inteiros, encontre o maior e o menor"""

array = [3, 7, 1, 9, 4]

# Um array que é preenchido pelo usuário
"""
array = list()
for i in renge(0, 5):
    valor_do_usuario = int(input("Digite um valor para o array: "))
    array.append(valor_do_usuario)
"""

#print(max(array))
#print(min(array)) Maneira fácil de fazer em python

maior = menor = array[0] # Ambos recebem o primeiro elemento do array (lista)

for valor in array:
    if maior < valor: # Se meu valor atual for menor que valor da posição do array
        maior = valor # Ele recebe esse novo valor
    elif menor > valor: # Mesma lógica da anterior
        menor = valor

print(f"Maior: {maior}\nMenor: {menor}") # Saída "Maior: 9" e "Menor: 1"