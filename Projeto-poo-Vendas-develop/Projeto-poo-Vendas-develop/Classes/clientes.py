from bancoDeDados import BancoDeDados

class Cliente:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = BancoDeDados()

    def menu(self):
        while True:
            print('\nOpções:')
            print('1 - Adicionar Cliente')
            print('2 - Listar Cliente')
            print('3 - Atualizar Cliente')
            print('4 - Deletar Cliente')
            print('0 - Sair')

            try:
                option = int(input('Escolha uma opção: '))
            except ValueError:
                print("Opção Inválida: entrada inválida. Por favor, digite um número inteiro.")

            if option == 1:
                self.adicionarClienteMenu()
            elif option == 2:
                self.listarClienteMenu()
            elif option == 3:
                self.atualizarClienteMenu()
            elif option == 4:
                self.deletarClienteMenu()
            elif option == 0:
                print("Saindo do menu Clientes.")
                break
            else:
                print("\n=============================================")
                print(f"Opção Inválida: opção '{option}' é inválida.")
                print("---------------------------------------------")
        return False

    def adicionarClienteMenu(self):
        nome = input("Digite o nome do Produto: ")
        email = input("Digite o preço do Produto: ")
    
        self.banco_de_dados.registerCliente(nome, email)
        print("Cliente adicionado com sucesso!")

    def listarClienteMenu(self):
        try:
            idCliente = int(input("Digite o ID do Cliente a ser lido: "))
            cliente = self.banco_de_dados.listCliente(idCliente)
            if cliente:
                print("=================================")
                print("Pedido encontrado:")
                print(f"ClienteID: {cliente[0]}")
                print(f"Nome: {cliente[1]}")
                print(f"Email: {cliente[2]}")
                print("=================================")
            else:
                print(f"Cliente com ID {idCliente} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número.")

    def atualizarClienteMenu(self):
        try:
            idCliente = int(input("Digite o ID do Cliente a ser atualizado: "))
            cliente = self.banco_de_dados.listCliente(idCliente)
            if cliente:
                print("=================================")
                print("Pedido encontrado:")
                print(f"ClienteID: {cliente[0]}")
                print(f"Nome: {cliente[1]}")
                print(f"Email: {cliente[2]}")
                print("=================================")

                nome = input("Digite o nome do Cliente: ")
                email = input("Digite o preço do Cliente: ")

                self.banco_de_dados.alterCliente(idCliente, nome, email)
                print(f"Cliente com ID {idCliente} atualizado com sucesso!")
            else:
                print(f"Cliente com ID {idCliente} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir números corretamente.")

    def deletarClienteMenu(self):
        try:
            idCliente = int(input("Digite o ID do Cliente a ser deletado: "))
            cliente = self.banco_de_dados.deleteCliente(idCliente)
            if cliente:
                confirmacao = input(f"Deseja realmente deletar o Cliente ID {idCliente}? (s/n): ").lower()
                if confirmacao == 's':
                    self.banco_de_dados.deleteCliente(idCliente)
                    print(f"Cliente com ID {idCliente} deletado com sucesso!")
                else:
                    print(f"Operação de exclusão cancelada para o Cliente ID {idCliente}.")
            else:
                print(f"Cliente com ID {idCliente} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número.")

    def endSystem(self):
        print("Sistema encerrado.")
        self.banco_de_dados.close_connection()
        exit()