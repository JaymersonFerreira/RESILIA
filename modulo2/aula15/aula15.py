# #Herança

# class Funcionario():
#     def __init__(self, nome, cpf, salario):
#         self.nome = nome
#         self.cpf = cpf
#         self.salario = salario

# class Gerente(Funcionario):
#     def __init__(self, senha, qtd_funcionarios):
#         self.senha = senha
#         self.qtd_funcionario = qtd_funcionarios

# gerente = Gerente('1234', 4)


#Polimorfismo

# class Funcionario():
#     cpf = ''
#     nome = ''

#     def comissao(self, valor):
#         print(valor * 0.5)

# class Gerrente(Funcionario):
#     def comissao(self, valor):
#         print(valor * 1.5)


# rafel  = Funcionario()
# luci = Gerrente()

# rafel.cpf = '111.111.111-00'
# # print(rafel.cpf = '111.111.111.00')

# print(rafel.cpf)

# rafel.comissao(100)
# luci.comissao(100)


class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn


class Ebook(Livro):
    def __init__(self, link_down):
        self.link_down = link_down
    
ebook = Ebook('link')

ebook.isbn = '1423'
ebook.titulo = 'nomeLivro'

print(ebook.isbn)
print(ebook.titulo)
