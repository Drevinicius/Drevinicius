def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b
def exibir_menu():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

def calcular():
    exibir_menu()
    operacao = input("Digite o número da operação desejada: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        print(soma(num1, num2))
    elif operacao == '2':
        print(subtracao(num1, num2))
    elif operacao == '3':
        print(multiplicacao(num1, num2))
    elif operacao == '4':
        print(divisao(num1, num2))
    else:
        print("Opção inválida")

# Executa a calculadora
calcular()-
