CREATE TABLE Cardapio (
    codigo_cardapio INT PRIMARY KEY AUTO_INCREMENT,
    nome_cafe VARCHAR(100) NOT NULL UNIQUE,
    descricao TEXT,
    preco_unitario DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Comanda (
    codigo_comanda INT PRIMARY KEY AUTO_INCREMENT,
    data DATETIME NOT NULL,
    numero_mesa INT,
    nome_cliente VARCHAR(150)
);

CREATE TABLE ItemComanda (
    codigo_comanda INT NOT NULL,
    codigo_cardapio INT NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade > 0),

    PRIMARY KEY (codigo_comanda, codigo_cardapio),

    FOREIGN KEY (codigo_comanda) REFERENCES Comanda(codigo_comanda),
    FOREIGN KEY (codigo_cardapio) REFERENCES Cardapio(codigo_cardapio)
);