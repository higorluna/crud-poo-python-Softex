-- Criação da base de dados
CREATE DATABASE IF NOT EXISTS vendas;
USE vendas;

-- Tabela de Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    ClienteID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100)
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


-- Inserir dados na tabela Clientes
INSERT INTO Clientes (Nome, Email) VALUES
('João Silva', 'joao@email.com'),
('Maria Souza', 'maria@email.com'),
('Pedro Oliveira', 'pedro@email.com'),
('Ana Santos', 'ana@email.com'),
('Carlos Pereira', 'carlos@email.com');


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


