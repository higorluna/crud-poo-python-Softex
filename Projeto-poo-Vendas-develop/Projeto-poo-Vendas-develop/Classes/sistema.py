from bancoDeDados import BancoDeDados
from pedidos import Pedido
from produtos import Produto

class SistemaPrincipal:
    def __init__(self) -> None:
        self.banco = BancoDeDados()
        self.pedido = Pedido(self.banco)
        self.produtos = Produto(self.banco)

    def menu(self):
        print('\nOpções:')
        print('1 - Menu de Produtos')
        print('2 - Menu de Clientes')
        print('3 - Menu de Pedidos')
        print('0 - Sair')

        option = input('Escolha uma opção: ')

        match option:
            case '1': # Ir para o Menu de Vendas
                self.produtos.menu()
            case '2': # Ir para o Menu de Clientes
                pass
            case '3': # Ir para o Menu de Pedidos
                self.pedido.menu()
                # pass
            case '0': # Exit
                return self.endSystem()
            case _:
                print("\n=============================================")
                print(f"Opção Inválida: opção '{option}' é inválida.")
                print("---------------------------------------------")

        return True
    
    def endSystem(self):
        return False


if __name__=="__main__":
    teste = SistemaPrincipal()
    teste.menu()
    pass