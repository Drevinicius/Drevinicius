"""Contador de vogais"""

vogais = 'aeiou'
texto = 'javascript'
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print(f"Número de vogais: {contador}") # Saída: 3