"""Receber uma lista e fazer a média aritmetica"""

array = [10, 20, 30]
media = 0 # inicio uma variavel auxiliar pra receber a média

for valor in array:
    media += valor # Soma os valores e soma a minha média

media = media/len(array)

print(f"Média de {array} é {media:.2f}") #  Saída: "Média de [10, 20, 30] é 20.00"