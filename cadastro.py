from time import sleep

class Interface:
    def __init__(self, actions):
        self.actions = actions

    def show_actions(self):
        print("=*" * 15)
        print(f"{'Nome':<8}{'Ação'}")
        for num, valor in enumerate(self.actions):
            print(f"{num + 1:<8}{valor}")
        print("=*" * 15)
        option = int(input("Escolha uma opção: "))
        print("=*" * 15)
        return option


class Cadastros:
    def __init__(self, nome, idade, lista):
        self.nome = nome
        self.idade = idade
        self.lista = lista

    def novo_cadastro(self):
        lista_de_cadastro = [self.nome, self.idade]
        return lista_de_cadastro

    def mostrar_cadastro(self):
        print("=*" * 15)
        print(f"{'Nomes':<15}{'Idades'}")
        for i in self.lista:
            print(f"{i[0]:<15}{i[1]}")
        sleep(2)

if __name__ == '__main__':
    lista_de_cadastro = list()
    while True:
        acoes_interface = ["Cadastrar", "Ver", "Sair"]
        interface = Interface(acoes_interface)
        opcao = interface.show_actions()

        if opcao == 1:
            cadastro = Cadastros(str(input("Nome para cadastro: ")), int(input("Idade para cadastro: ")), [])
            novo = cadastro.novo_cadastro()
            lista_de_cadastro.append(novo)

        elif opcao == 2:
            cadastro1 = Cadastros("", 0, lista_de_cadastro)
            cadastro1.mostrar_cadastro()

        elif opcao == 3:
            print("Finalizando")
            for i in range(1, 4):
                sleep(1)
                print(i, end="...", flush=True)
            sleep(1)
            print("Fim", flush=False)
            sleep(0.6)
            break
