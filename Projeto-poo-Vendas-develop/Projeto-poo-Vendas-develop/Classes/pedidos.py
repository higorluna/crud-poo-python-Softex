class Pedido:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def menu(self):
        while True:
            print('\nOpções:')
            print('1 - Criar Pedido')
            print('2 - Ler Pedido por ID')
            print('3 - Atualizar Pedido')
            print('4 - Deletar Pedido')
            print('0 - Sair')

            option = input('Escolha uma opção: ')

            if option == '1':
                self.criar_pedido_menu()
            elif option == '2':
                self.ler_pedido_menu()
            elif option == '3':
                self.atualizar_pedido_menu()
            elif option == '4':
                self.deletar_pedido_menu()
            elif option == '0':
                print("Saindo do menu de pedidos.")
                break
            else:
                print("\n=============================================")
                print(f"Opção Inválida: opção '{option}' é inválida.")
                print("---------------------------------------------")
        return False

    def criar_pedido_menu(self):
        cliente_id = int(input("Digite o ID do Cliente: "))
        data_pedido = '2024-08-06'
        valor_total = float(input("Digite o novo Valor Total: "))
        status = input("Digite o Status do processo: ")

        self.banco_de_dados.criar_pedido(cliente_id, valor_total, status, data_pedido)
        print("Pedido criado com sucesso!")

    def ler_pedido_menu(self):
        try:
            pedido_id = int(input("Digite o ID do Pedido a ser lido: "))
            pedido = self.banco_de_dados.ler_pedido(pedido_id)
            if pedido:
                print("=================================")
                print("Pedido encontrado:")
                print(f"PedidoID: {pedido[0]}")
                print(f"ClienteID: {pedido[1]}")
                print(f"Data do Pedido: {pedido[2]}")
                print(f"Valor Total: {pedido[3]}")
                print(f"Status: {pedido[4]}")
                print("=================================")
            else:
                print(f"Pedido com ID {pedido_id} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número.")

    def atualizar_pedido_menu(self):
        try:
            pedido_id = int(input("Digite o ID do Pedido a ser atualizado: "))
            pedido = self.banco_de_dados.ler_pedido(pedido_id)
            if pedido:
                print("=================================")
                print("Pedido encontrado:")
                print(f"PedidoID: {pedido[0]}")
                print(f"ClienteID: {pedido[1]}")
                print(f"Data do Pedido: {pedido[2]}")
                print(f"Valor Total: {pedido[3]}")
                print(f"Status: {pedido[4]}")
                print("=================================")

                #cliente_id, data_pedido, valor_total, status
                cliente_id = int(input("Digite o ID do Cliente: "))
                data_pedido = '2024-08-06'
                valor_total = float(input("Digite o novo Valor Total: "))

                self.banco_de_dados.atualizar_pedido(pedido_id, cliente_id, data_pedido, valor_total)
                print(f"Pedido com ID {pedido_id} atualizado com sucesso!")
            else:
                print(f"Pedido com ID {pedido_id} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir números corretamente.")

    def deletar_pedido_menu(self):
        try:
            pedido_id = int(input("Digite o ID do Pedido a ser deletado: "))
            pedido = self.banco_de_dados.ler_pedido(pedido_id)
            if pedido:
                confirmacao = input(f"Deseja realmente deletar o Pedido ID {pedido_id}? (s/n): ").lower()
                if confirmacao == 's':
                    self.banco_de_dados.deletar_pedido(pedido_id)
                    print(f"Pedido com ID {pedido_id} deletado com sucesso!")
                else:
                    print(f"Operação de exclusão cancelada para o Pedido ID {pedido_id}.")
            else:
                print(f"Pedido com ID {pedido_id} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número.")

    def endSystem(self):
        print("Sistema encerrado.")
        self.banco_de_dados.close_connection()
        exit()
