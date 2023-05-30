# class Cliente():
#     def __init__(self, nome, sobrenome, cpf):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.cpf = cpf

#     # def get_nome(self):
#     #     return self.nome

# class Conta():
#     def __init__(self, numero, cliente, saldo, limite):
#         self.numero = numero
#         self.titular = cliente
#         self.saldo = saldo
#         self.limite = limite


# cliente = Cliente('rafael', 'pilan', '111.333.222-00')

# # print(Cliente.get_nome)
# minha_conta = Conta('123-4', cliente, 120.0, 500.0)

# print(minha_conta.titular.cpf)
# print(minha_conta.saldo)

class Historico():
    def __init__(self):
        self.data_abertura = ''
        self.transacoes = []

class Conta():
    def __init__(self):
        self.cliente = ''
        self.historico = Historico()

minha_conta = Conta()
minha_conta.cliente = 'rafael'
minha_conta.historico.transacoes = [1, 2, 3]
minha_conta.historico.data_abertura = '30/05/2023'

print(minha_conta.historico.transacoes)
print(minha_conta.cliente)
print(minha_conta.historico.data_abertura)