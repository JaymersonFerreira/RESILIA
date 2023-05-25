# class Gato():
#     nome = 'jayme'
#     dataDeNascimento = ''
#     raca = ''

#     def miar(self, nome):
#         print('O gato', nome, 'miou!!!')

#     def comer(self, nome):
#         print('O gato', nome, 'comeu!!!')


# miau = Gato()

# miau.nome = 'cat'
# miau.dataDeNascimento = '19/03/2020'
# miau.raca = 'frajola'
# miau.miar(miau.nome)
# miau.comer(miau.nome)
# print(miau.nome)
# print(miau.dataDeNascimento)
# print(miau.raca)

# class InfPessoa():
#     idade = ''
#     cidade = ''
#     estado = ''
#     salarioAtual = ''
#     escolaridade = ''

#     def printInf(self, idade, cidade, estado, salarioAtual, escolaridade):
#         print(f"Você tem {idade} anos mora no estado {estado} Cidade: {cidade}, Salario: {salarioAtual}, Escolaridade: {escolaridade}")

# pessoa = InfPessoa()

# pessoa.idade = input("Informe sua idade:")
# pessoa.cidade = input("Informe sua cidade:")
# pessoa.estado = input("Informe seu estado:")
# pessoa.salarioAtual = input("Informe seu salarioAtual:")
# pessoa.escolaridade = input("Informe sua escolaridade:")
# pessoa.printInf(pessoa.idade, pessoa.cidade, pessoa.estado, pessoa.salarioAtual, pessoa.escolaridade)

instrumento_musicais = 'guitarra, bateria, baixo, teclado'

lista_instrumentos = instrumento_musicais.split(',')
print(lista_instrumentos)

lista_instrumentos = instrumento_musicais.split(';')
print(lista_instrumentos)
# ['guitarra', 'bateria', 'baixo', 'teclado']