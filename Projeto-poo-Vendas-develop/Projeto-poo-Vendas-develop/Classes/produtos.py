class Produto:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def menu(self):
        while True:
            print('\nOpções:')
            print('1 - Adicionar Produto')
            print('2 - Listar Produtos')
            print('3 - Atualizar Produto')
            print('4 - Deletar Produto')
            print('0 - Sair')

            try:
                option = int(input('Escolha uma opção: '))
            except ValueError:
                print("Opção Inválida: entrada inválida. Por favor, digite um número inteiro.")

            if option == 1:
                self.adicionarProduto()
            elif option == 2:
                self.listarProdutos()
            elif option == 3:
                self.atualizarProduto()
            elif option == 4:
                self.deletarProduto()
            elif option == 0:
                print("Saindo do menu produtos.")
                break
            else:
                print("\n=============================================")
                print(f"Opção Inválida: opção '{option}' é inválida.")
                print("---------------------------------------------")
        return False

    def adicionarProdutoMenu(self):
        nomeProduto = input("Digite o nome do Produto: ")
        preco = int(input("Digite o preço do Produto: "))
        estoque = int(input("Digite a quantidade total do estoque: "))
    
        self.banco_de_dados.adicionarProduto(nomeProduto, preco, estoque)
        print("Produto criado com!")

    def listarProduto(self):
        try:
            idProduto = int(input("Digite o ID do Pedido a ser lido: "))
            produto = self.banco_de_dados.listarProduto(idProduto)
            if produto:
                print("=================================")
                print("Pedido encontrado:")
                print(f"PedidoID: {produto[0]}")
                print(f"ClienteID: {produto[1]}")
                print(f"Data do Pedido: {produto[2]}")
                print(f"Valor Total: {produto[3]}")
                print(f"Status: {produto[4]}")
                print("=================================")
            else:
                print(f"Pedido com ID {idProduto} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número.")

    def atualizarProduto(self):
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

    def deletarProduto(self):
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