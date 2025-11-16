-- Faça uma listagem do cardápio ordenada por nome
SELECT 
    codigo_cardapio, 
    nome_cafe, 
    descricao, 
    preco_unitario
FROM 
    Cardapio
ORDER BY 
    nome_cafe ASC;

-- Apresente todas as comandas e os itens da comanda
SELECT 
    C.codigo_comanda,
    C.data,
    C.numero_mesa,
    C.nome_cliente,
    M.nome_cafe,
    M.descricao,
    IC.quantidade,
    M.preco_unitario,
    (IC.quantidade * M.preco_unitario) AS preco_total_item
FROM 
    Comanda AS C
JOIN 
    ItemComanda AS IC ON C.codigo_comanda = IC.codigo_comanda
JOIN 
    Cardapio AS M ON IC.codigo_cardapio = M.codigo_cardapio
ORDER BY 
    C.data, 
    C.codigo_comanda, 
    M.nome_cafe;

-- Liste todas as comandas, mais uma coluna com o valor total da comanda
SELECT 
    C.codigo_comanda,
    C.data,
    C.numero_mesa,
    C.nome_cliente,
    SUM(IC.quantidade * M.preco_unitario) AS valor_total_comanda
FROM 
    Comanda AS C
JOIN 
    ItemComanda AS IC ON C.codigo_comanda = IC.codigo_comanda
JOIN 
    Cardapio AS M ON IC.codigo_cardapio = M.codigo_cardapio
GROUP BY 
    C.codigo_comanda, 
    C.data, 
    C.numero_mesa, 
    C.nome_cliente
ORDER BY 
    C.data;

-- Traga apenas as comandas que possuem mais do que um tipo de café
SELECT 
    C.codigo_comanda,
    C.data,
    C.numero_mesa,
    C.nome_cliente,
    SUM(IC.quantidade * M.preco_unitario) AS valor_total_comanda
FROM 
    Comanda AS C
JOIN 
    ItemComanda AS IC ON C.codigo_comanda = IC.codigo_comanda
JOIN 
    Cardapio AS M ON IC.codigo_cardapio = M.codigo_cardapio
GROUP BY 
    C.codigo_comanda, 
    C.data, 
    C.numero_mesa, 
    C.nome_cliente
HAVING 
    COUNT(IC.codigo_cardapio) > 1
ORDER BY 
    C.data;

-- Qual o total de faturamento por data?
SELECT 
    DATE(C.data) AS data_venda,
    SUM(IC.quantidade * M.preco_unitario) AS faturamento_total_dia
FROM 
    Comanda AS C
JOIN 
    ItemComanda AS IC ON C.codigo_comanda = IC.codigo_comanda
JOIN 
    Cardapio AS M ON IC.codigo_cardapio = M.codigo_cardapio
GROUP BY 
    DATE(C.data)
ORDER BY 
    data_venda;