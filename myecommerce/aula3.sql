-- inserir registros
INSERT INTO PRODUCTS(ID, NAME, DESCRIPTION, CATEGORY, PRICE, IN_STOCK)
VALUES (1, 'Computador', 'Computador 8 nuclues Gamer', 'Informatica', 2600, 't');

-- inserir registros
INSERT INTO PRODUCTS(ID, NAME, DESCRIPTION, CATEGORY, PRICE, IN_STOCK)
VALUES (2, 'Celulas', 'Celular Dual Chip', 'Eletronico', 1250, 't');

--mostra tabela
SELECT * FROM PRODUCTS;

-- apaga a tabela
drop table products

-- CRIA A TABELA
CREATE TABLE PRODUCTS(
	ID INT,
	NAME VARCHAR(60),
	DESCRIPTION VARCHAR(150),
	CATEGORY VARCHAR(40),
	PRICE NUMERIC(10,2),
	IN_STOCK BOOLEAN
);

-- inserir registros
insert into products (id, name, description, category, price, in_stock) values (1, 'Computador', 'Computador Gamer 8 Nucleos', 'Informatica', 2600, 't');
insert into products (id, name, description, category, price, in_stock) values (2, 'Celular', 'Celular Dualchip', 'Eletronico', 1250, 't');
insert into products (id, name, description, category, price, in_stock) values (3, 'Ventilador', 'Ventilador 4 velocidades', 'Eletrodomestico', 180.90, 'f');
insert into products (id, name, description, category, price, in_stock) values (4, 'Televisor', 'Televisor Smart 42 pol.', 'Eletroeletronico', 1750.60, 't');
insert into products (id, name, description, category, price, in_stock) values (5, 'Mouse', 'Mouse sem fio', 'Informatica', 38, 't');
insert into products (id, name, description, category, price, in_stock) values (6, 'Bicicleta', 'Bicicleta Mtb Aro 29', 'Esporte', 1360, 't');
insert into products (id, name, description, category, price, in_stock) values (7, 'Geladeira', 'Geladeira Duplex', 'Eletrodomestico', 2230.0, 't');
insert into products (id, name, description, category, price, in_stock) values (8, 'Ar condicionado', 'Ar Condicionado Split 12000 Btus', 'Eletrodomestico', 1890.0, 'f');
insert into products (id, name, description, category, price, in_stock) values (9, 'Raquete de tênis', 'Raquete de tênis Graphene 360+', 'Esporte', 670.0, 'f');
insert into products (id, name, description, category, price, in_stock) values (10, 'Sofá', 'Sofá Retrátil e Reclinável', 'Moveis', 1245.0, 't');
insert into products (id, name, description, category, price, in_stock) values (11, 'Cama box', 'Cama box conjugado casal', 'Moveis', 580.0, 'f');
insert into products (id, name, description, category, price, in_stock) values (12, 'Mesa', 'Mesa de jantar c/ 4 cadeiras', 'Moveis', 480.0, 't');
insert into products (id, name, description, category, price, in_stock) values (13, 'Microfone', 'Microfone condensador', 'Eletronico', 380.0, 't');
insert into products (id, name, description, category, price, in_stock) values (14, 'Mesa de tênis', 'Mesa de tênis ping pong', 'Esporte', 723.0, 't');
insert into products (id, name, description, category, price, in_stock) values (15, 'Cafeteira', 'Cafeteira expresso automática', 'Eletrodomestico', 450.0, 't');

--mostra tabela
SELECT * FROM PRODUCTS;

--atualiza um registo
UPDATE PRODUCTS SET PRICE = 230.50, IN_STOCK = 'f'
WHERE ID = 3;

--mostra tabela
SELECT * FROM PRODUCTS;

--atualiza um registo
UPDATE PRODUCTS SET DESCRIPTION = 'Computador Quad Core Gamer' WHERE ID = 1;

--mostra tabela
SELECT * FROM PRODUCTS;

-- deletar um registro
DELETE FROM PRODUCTS WHERE ID = 6;

--mostra tabela
SELECT * FROM PRODUCTS;




