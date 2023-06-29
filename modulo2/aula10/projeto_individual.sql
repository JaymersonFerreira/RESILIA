-- tabela empresas
CREATE TABLE empresas (
  id INT PRIMARY KEY,
  nome VARCHAR(255),
  cnpj VARCHAR (14),
  endereco VARCHAR(255),
  telefone VARCHAR(20)
);

-- tabela tecnologias
CREATE TABLE tecnologias (
  id INT PRIMARY KEY,
  nome VARCHAR(255),
  area_atuacao VARCHAR(50)
);

-- tabela colaboradores
CREATE TABLE colaboradores (
  id INT PRIMARY KEY,
  nome VARCHAR(255),
  cpf VARCHAR(11),
  cargo VARCHAR(50),
  telefone VARCHAR(20),
  empresa_id INT,
  FOREIGN KEY (empresa_id) REFERENCES empresas(id)
);

-- tabela tecnologias_empresas
CREATE TABLE empresas_tecnologias (
  id INT PRIMARY KEY,
  empresa_id INT,
  tecnologia_id INT,
  FOREIGN KEY (empresa_id) REFERENCES empresas(id),
  FOREIGN KEY (tecnologia_id) REFERENCES tecnologias(id)
);
-- inserindo dados empresas
INSERT INTO empresas (nome, cnpj, endereco, telefone)
VALUES ('creativa web', '12345678910111' , 'rua cachorro malhado, numero: 66', '5050505050'),
       ('futuro dev', '12345678910111', 'rua enche linguiça, numero 00', '0112223333');
-- inserindo dados tecnologias
INSERT INTO tecnologias (nome, area_atuacao)
VALUES ('nasa', 'Web'),
       ('pentagono', 'Dados');
-- inserindo dados colaboradores
INSERT INTO colaboradores (nome, cpf, cargo, empresa_id)
VALUES ('jaymerson', '15123564878', 'cio', 1),
       ('sr. ferreira', '15123564878', 'cto', 2);
