import mysql.connector

class BancoDeDados:
    def __init__(self) -> None:
        self.config = {
            'user': 'root',
            'password': 'j1l2a3h4',
            'host': 'localhost', 
            'database': 'vendas',
            'raise_on_warnings': True
        }
        self.conn = self.connectToDatabase()

    def connectToDatabase(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            # print("Conexão Estabelecida com Sucesso")
            return self.conn
        except:
            print("Não foi possivel estabelecer conexão com o banco de dados")
            return False

    def closeConnection(self):
        self.cursor.close()
        pass

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return None
        finally:
            cursor.close()

    # ===========
    def criar_pedido(self, cliente_id, valor_total, status, data_pedido='2024-08-06'):
        query = '''
            INSERT INTO pedidos (ClienteID, DataPedido, ValorTotal, Status)
            VALUES (%s, %s, %s, %s)
        '''
        params = (cliente_id, data_pedido, valor_total, status)  # Corrigido o posicionamento dos parâmetros
        self.execute_query(query, params)


    def atualizar_pedido(self,pedido_id, cliente_id, data_pedido, valor_total):
        query = '''
            UPDATE pedidos
            SET ClienteID = %s, DataPedido = %s, ValorTotal = %s
            WHERE PedidoID = %s
        '''
        params = (cliente_id, data_pedido, valor_total, pedido_id)
        self.execute_query(query, params)

    def deletar_pedido(self, pedido_id):
        query = 'DELETE FROM pedidos WHERE PedidoID = %s'
        self.execute_query(query, (pedido_id,))

    def ler_pedido(self, pedido_id):
        try:
            sql = "SELECT * FROM pedidos WHERE PedidoID = %s"
            self.cursor.execute(sql, (pedido_id,))
            pedido = self.cursor.fetchone()
            return pedido
        except mysql.connector.Error as err:
            print(f"Erro ao ler pedido: {err}")
            return None
        
    def adicionarProduto(self, nomeProduto, preco, estoque):
        query = '''
            INSERT INTO Produtos (Nome, Preco, Estoque)
            VALUES (%s, %s, %s)
        '''
        params = (nomeProduto, preco, estoque)  
        self.execute_query(query, params)

    def listarProduto(self, idProduto):
        try:
            sql = "SELECT * FROM Produtos WHERE ProdutoID = %s"
            self.cursor.execute(sql, (idProduto,))
            produto = self.cursor.fetchone()
            return produto
        except mysql.connector.Error as err:
            print(f"Erro ao ler produto: {err}")
            return None
        
    def atualizarProduto(self,idProduto, nomeProduto, preco, estoque):
        query = '''
            UPDATE Produtos
            SET Nome = %s, Preco = %s, Estoque = %s
            WHERE ProdutoID = %s
        '''
        params = (nomeProduto, preco, estoque, idProduto)
        self.execute_query(query, params)

    def deletarProduto(self, idProduto):
        query = 'DELETE FROM Produtos WHERE ProdutoID = %s'
        self.execute_query(query, (idProduto,))
    
    def registerCliente(self, nome, email):
        query = '''
            INSERT INTO Clientes (Nome, Email)
            VALUES (%s, %s)
        '''
        params = (nome, email)  
        self.execute_query(query, params)
        
    def listCliente(self, idCliente):
        try:
            sql = "SELECT * FROM Clientes WHERE ClienteID = %s"
            self.cursor.execute(sql, (idCliente,))
            cliente = self.cursor.fetchone()
            return cliente
        except mysql.connector.Error as err:
            print(f"Erro ao ler cliente: {err}")
            return None
    
    def alterCliente(self,idCliente, nome, email):
        query = '''
            UPDATE Produtos
            SET Nome = %s, Email = %s
            WHERE ClienteID = %s
        '''
        params = (nome, email, idCliente)
        self.execute_query(query, params)
    
    def deleteCliente(self, idCliente):
        query = 'DELETE FROM Clientes WHERE ClienteID = %s'
        self.execute_query(query, (idCliente,))
        
if __name__=="__main__":
    init = BancoDeDados()
  