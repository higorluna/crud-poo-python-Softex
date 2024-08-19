-- Criação da base de dados
CREATE DATABASE IF NOT EXISTS vendas;
USE vendas;

-- Tabela de Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    ClienteID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    Telefone VARCHAR(20)
);

-- Tabela de Produtos
CREATE TABLE IF NOT EXISTS Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    Estoque INT NOT NULL
);

-- Tabela de Pedidos
CREATE TABLE IF NOT EXISTS Pedidos (
    PedidoID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT NOT NULL,
    DataPedido DATE NOT NULL,
    ValorTotal DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

-- Tabela de Itens de Pedido
CREATE TABLE IF NOT EXISTS ItensPedido (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,
    PedidoID INT NOT NULL,
    ProdutoID INT NOT NULL,
    Quantidade INT NOT NULL,
    PrecoUnitario DECIMAL(10, 2) NOT NULL,
    TotalItem DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (PedidoID) REFERENCES Pedidos(PedidoID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);


-- Inserir dados na tabela Clientes
INSERT INTO Clientes (Nome, Email, Telefone) VALUES
('João Silva', 'joao@email.com', '(11) 1234-5678'),
('Maria Souza', 'maria@email.com', '(21) 9876-5432'),
('Pedro Oliveira', 'pedro@email.com', '(31) 9999-8888'),
('Ana Santos', 'ana@email.com', '(41) 8765-4321'),
('Carlos Pereira', 'carlos@email.com', '(51) 7654-3210'),
('Juliana Costa', 'juliana@email.com', '(61) 6543-2109'),
('Fernando Almeida', 'fernando@email.com', '(71) 5432-1098'),
('Luiza Ferreira', 'luiza@email.com', '(81) 4321-0987'),
('Rafael Lima', 'rafael@email.com', '(91) 3210-9876'),
('Mariana Oliveira', 'mariana@email.com', '(32) 2109-8765'),
('Rodrigo Santos', 'rodrigo@email.com', '(42) 1098-7654'),
('Cristina Costa', 'cristina@email.com', '(52) 0987-6543'),
('Diego Silva', 'diego@email.com', '(62) 9876-5432'),
('Patrícia Souza', 'patricia@email.com', '(72) 8765-4321'),
('Renato Pereira', 'renato@email.com', '(82) 7654-3210');


-- Inserir dados na tabela Produtos
INSERT INTO Produtos (Nome, Preco, Estoque) VALUES
('Camiseta Branca', 29.90, 100),
('Calça Jeans', 89.90, 50),
('Tênis Esportivo', 149.90, 30),
('Mochila Grande', 99.90, 20),
('Óculos de Sol', 79.90, 40),
('Relógio Analógico', 199.90, 15),
('Fone de Ouvido Bluetooth', 129.90, 25),
('Cadeira de Escritório', 299.90, 10),
('Mesa de Jantar', 399.90, 8),
('Notebook', 2499.90, 5),
('Smartphone', 1799.90, 12),
('Impressora Multifuncional', 499.90, 7),
('Câmera Fotográfica', 899.90, 6),
('Tablet', 899.90, 9),
('Ventilador de Teto', 149.90, 15),
('Liquidificador', 79.90, 20),
('Forno Elétrico', 299.90, 12),
('Aspirador de Pó', 199.90, 18),
('Churrasqueira Elétrica', 199.90, 10),
('Panela de Pressão', 89.90, 25),
('Jogo de Panelas', 199.90, 15),
('Conjunto de Facas', 49.90, 30),
('Secador de Cabelo', 69.90, 20),
('Massageador', 129.90, 15),
('Caixa de Som Bluetooth', 149.90, 25),
('Escova Elétrica', 59.90, 35),
('Batedeira', 129.90, 15),
('Máquina de Café', 199.90, 10),
('Robô Aspirador', 299.90, 8),
('Monitor Gamer', 999.90, 6);


-- Inserir mais 40 Pedidos fictícios
INSERT INTO Pedidos (ClienteID, DataPedido, ValorTotal, Status) VALUES
(6, '2024-08-06', 180.00, 'Pago'),
(7, '2024-08-07', 210.00, 'Pago'),
(8, '2024-08-08', 300.00, 'Enviado'),
(9, '2024-08-09', 90.00, 'Pago'),
(10, '2024-08-10', 420.00, 'Em processamento'),
(11, '2024-08-11', 150.00, 'Pago'),
(12, '2024-08-12', 280.00, 'Pago'),
(13, '2024-08-13', 360.00, 'Enviado'),
(14, '2024-08-14', 200.00, 'Pago'),
(15, '2024-08-15', 240.00, 'Em processamento'),
(3, '2024-08-16', 130.00, 'Pago'),
(3, '2024-08-17', 380.00, 'Pago'),
(4, '2024-08-18', 270.00, 'Enviado'),
(5, '2024-08-19', 110.00, 'Pago'),
(1, '2024-08-20', 450.00, 'Em processamento'),
(1, '2024-08-21', 140.00, 'Pago'),
(2, '2024-08-22', 320.00, 'Pago'),
(3, '2024-08-23', 410.00, 'Enviado'),
(4, '2024-08-24', 160.00, 'Pago'),
(5, '2024-08-25', 290.00, 'Em processamento'),
(6, '2024-08-26', 170.00, 'Pago'),
(7, '2024-08-27', 220.00, 'Pago'),
(8, '2024-08-28', 310.00, 'Enviado'),
(9, '2024-08-29', 100.00, 'Pago'),
(10, '2024-08-30', 430.00, 'Em processamento'),
(11, '2024-08-31', 120.00, 'Pago'),
(12, '2024-09-01', 290.00, 'Pago'),
(13, '2024-09-02', 370.00, 'Enviado'),
(14, '2024-09-03', 190.00, 'Pago'),
(15, '2024-09-04', 250.00, 'Em processamento'),
(6, '2024-09-05', 140.00, 'Pago'),
(5, '2024-09-06', 390.00, 'Pago'),
(4, '2024-09-07', 280.00, 'Enviado'),
(3, '2024-09-08', 120.00, 'Pago'),
(2, '2024-09-09', 460.00, 'Em processamento'),
(1, '2024-09-10', 150.00, 'Pago'),
(2, '2024-09-11', 330.00, 'Pago'),
(3, '2024-09-12', 420.00, 'Enviado'),
(4, '2024-09-13', 170.00, 'Pago'),
(5, '2024-09-14', 300.00, 'Em processamento');


-- Inserir detalhamento de itens para os próximos 40 pedidos (IDs de 41 a 80)

-- Itens para PedidoID 44
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (44, 9, 1, 79.90, 79.90),
       (44, 10, 2, 49.90, 99.80),
       (44, 11, 1, 199.90, 199.90);

-- Itens para PedidoID 45
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (45, 12, 1, 299.90, 299.90),
       (45, 13, 1, 129.90, 129.90);

-- Itens para PedidoID 46
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (46, 14, 2, 59.90, 119.80),
       (46, 12, 1, 89.90, 89.90);

-- Itens para PedidoID 47
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (47, 11, 1, 179.90, 179.90),
       (47, 7, 3, 39.90, 119.70),
       (47, 6, 1, 249.90, 249.90);

-- Itens para PedidoID 48
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (48, 4, 1, 149.90, 149.90),
       (48, 1, 1, 179.90, 179.90),
       (48, 11, 2, 69.90, 139.80);

-- Itens para PedidoID 49
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (49, 12, 1, 99.90, 99.90),
       (49, 2, 1, 159.90, 159.90);

-- Itens para PedidoID 50
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (50, 14, 1, 199.90, 199.90),
       (50, 15, 2, 119.90, 239.80);

-- Itens para PedidoID 51
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (51, 7, 1, 169.90, 169.90),
       (51, 14, 1, 89.90, 89.90);

-- Itens para PedidoID 52
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (52, 11, 1, 249.90, 249.90),
       (52, 7, 1, 179.90, 179.90),
       (52, 3, 1, 129.90, 129.90);

-- Itens para PedidoID 53
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (53, 1, 1, 99.90, 99.90),
       (53, 12, 2, 69.90, 139.80);

-- Itens para PedidoID 54
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (54, 13, 1, 149.90, 149.90),
       (54, 14, 1, 199.90, 199.90);

-- Itens para PedidoID 55
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (55, 2, 1, 129.90, 129.90),
       (55, 1, 3, 59.90, 179.70),
       (55, 12, 1, 109.90, 109.90);

-- Itens para PedidoID 56
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (56, 13, 1, 89.90, 89.90),
       (56, 9, 1, 179.90, 179.90);

-- Itens para PedidoID 57
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (57, 4, 2, 49.90, 99.80),
       (57, 1, 1, 159.90, 159.90);

-- Itens para PedidoID 58
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (58, 12, 1, 199.90, 199.90),
       (58, 13, 1, 149.90, 149.90);

-- Itens para PedidoID 59
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (59, 14, 1, 79.90, 79.90),
       (59, 15, 2, 69.90, 139.80);

-- Itens para PedidoID 60
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (60, 6, 1, 129.90, 129.90),
       (60, 7, 1, 179.90, 179.90),
       (60, 8, 1, 249.90, 249.90);

-- Itens para PedidoID 61
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (61, 9, 1, 299.90, 299.90),
       (61, 5, 1, 129.90, 129.90);

-- Itens para PedidoID 62
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (62, 1, 1, 179.90, 179.90),
       (62, 12, 2, 99.90, 199.80);

-- Itens para PedidoID 63
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (63, 13, 1, 149.90, 149.90),
       (63, 14, 1, 179.90, 179.90);

-- Itens para PedidoID 64
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (64, 5, 1, 199.90, 199.90),
       (64, 6, 1, 89.90, 89.90),
       (64, 7, 1, 129.90, 129.90);

-- Itens para PedidoID 65
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (65, 1, 2, 49.90, 99.80),
       (65, 2, 1, 159.90, 159.90);

-- Itens para PedidoID 66
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (66, 3, 1, 199.90, 199.90),
       (66, 4, 1, 179.90, 179.90),
       (66, 2, 1, 149.90, 149.90);

-- Itens para PedidoID 67
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (67, 5, 1, 129.90, 129.90),
       (67, 4, 2, 69.90, 139.80);

-- Itens para PedidoID 68
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario, TotalItem)
VALUES (68, 5, 1, 199.90, 199.90),
       (68, 6, 1, 89.90, 89.90);
