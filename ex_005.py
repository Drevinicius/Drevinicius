"""Inverter uma string"""

texto = "programar"
texto_inverso = str()
# texto_inverso = texto[::-1] Maneira fácil

for i in range(len(texto)-1, -1, -1):
    texto_inverso += texto[i]

print(texto_inverso)