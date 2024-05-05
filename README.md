from random import randint, choice
from time import sleep
cor = {
    'limpa':'\033[m',
    'vermelho':'\033[1;31m'
}
def numerico():
    dig = str(input('Quantos digitos têm sua senha? 4, 5 ou 6: ')).strip()
    print('Gerando a senha...')
    sleep(3)
    if dig == '4':
        senha = randint(1000, 9999)
    elif dig == '5':
        senha = randint(10000, 99999)
    else:
        senha = randint(100000, 999999)
    print(f'Sua senha é {cor["vermelho"]}{senha:.0f}{cor['limpa']}') 
def alfanumerico():
    print('Gerando senha...')
    sleep(3)
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    esc1 = choice(letras)
    esc2 = choice(letras)
    num1 = randint(10, 99)
    num2 = randint(10, 90)
    print(f'A senha alfanumerica têm 6 digitos, sendo {cor['vermelho']}{num1:.0f}{esc1}{num2:.0f}{esc2}{cor['limpa']}')
print('-=' * 20)
print('GERADOR DE SENHA NUMERICA/ ALFANUMERICO')
print('-=' * 20)
escolha = str(input('Qual o estilo da senha? N (numerica) ou A (Alfanumerica): ')).strip().upper()
if escolha == 'N':
    numerico()
else:
    alfanumerico()
