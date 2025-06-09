"""Identificador de palindromos"""

texto = "radar"
texto_inverso = texto[::-1] # Recebe o texto inverso

print("É palindromo" if texto_inverso == texto else "Não é palindromo") # Saída: É palindromo