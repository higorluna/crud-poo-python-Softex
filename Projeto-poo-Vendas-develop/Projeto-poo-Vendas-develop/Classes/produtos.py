from bancoDeDados import BancoDeDados
class Produto:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = BancoDeDados()

    def menu(self):
        while True:
            print('\nOpções:')
            print('1 - Adicionar Produto')
            print('2 - Listar Produto')
            print('3 - Atualizar Produto')
            print('4 - Deletar Produto')
            print('0 - Sair')

            try:
                option = int(input('Escolha uma opção: '))
            except ValueError:
                print("Opção Inválida: entrada inválida. Por favor, digite um número inteiro.")

            if option == 1:
                self.adicionarProdutoMenu()
            elif option == 2:
                self.listarProdutoMenu()
            elif option == 3:
                self.atualizarProdutoMenu()
            elif option == 4:
                self.deletarProdutoMenu()
            elif option == 0:
                print("Saindo do menu Produtos.")
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
        print("Produto criado com sucesso!")

    def listarProdutoMenu(self):
        try:
            idProduto = int(input("Digite o ID do Produto a ser lido: "))
            produto = self.banco_de_dados.listarProduto(idProduto)
            if produto:
                print("=================================")
                print("Pedido encontrado:")
                print(f"ProdutoID: {produto[0]}")
                print(f"Nome do Produto: {produto[1]}")
                print(f"Preco: {produto[2]}")
                print(f"Estoque: {produto[3]}")
                print("=================================")
            else:
                print(f"Produto com ID {idProduto} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número.")

    def atualizarProdutoMenu(self):
        try:
            idProduto = int(input("Digite o ID do Produto a ser atualizado: "))
            produto = self.banco_de_dados.listarProduto(idProduto)
            if produto:
                print("=================================")
                print("Pedido encontrado:")
                print(f"ProdutoID: {produto[0]}")
                print(f"Nome do Produto: {produto[1]}")
                print(f"Preco: {produto[2]}")
                print(f"Estoque: {produto[3]}")
                print("=================================")

                nomeProduto = input("Digite o nome do Produto: ")
                preco = int(input("Digite o preço do Produto: "))
                estoque = int(input("Digite a quantidade total do estoque: "))

                self.banco_de_dados.atualizarProduto(idProduto, nomeProduto, preco, estoque)
                print(f"Produto com ID {idProduto} atualizado com sucesso!")
            else:
                print(f"Produto com ID {idProduto} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir números corretamente.")

    def deletarProdutoMenu(self):
        try:
            idProduto = int(input("Digite o ID do Produto a ser deletado: "))
            produto = self.banco_de_dados.listarProduto(idProduto)
            if produto:
                confirmacao = input(f"Deseja realmente deletar o Produto ID {idProduto}? (s/n): ").lower()
                if confirmacao == 's':
                    self.banco_de_dados.deletarProduto(idProduto)
                    print(f"Produto com ID {idProduto} deletado com sucesso!")
                else:
                    print(f"Operação de exclusão cancelada para o Produto ID {idProduto}.")
            else:
                print(f"Produto com ID {idProduto} não encontrado.")
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número.")

    def endSystem(self):
        print("Sistema encerrado.")
        self.banco_de_dados.closeConnection()
        exit()