# class Conta():
#     def __init__(self, saldo):
#         self._saldo = saldo

#     def get_saldo(self):
#         return self._saldo
    
#     def set_saldo(self, saldo):
#         self._saldo = saldo

# conta1 = Conta(200.00)
# conta2 = Conta(300.00)
# conta3 = Conta(-100.00)

# print(conta1.get_saldo())
# print(conta2.get_saldo())
# print(conta3.get_saldo())

class Pessoa():
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        set._nome = nome

    def get_cpf(self):
        return self._cpf
    
    def set_cpf(self, cpf):
        set._cpf = cpf


pessoa = Pessoa('joao', '000.000.000-00')

nome = pessoa.get_nome()
nome = 'joão'
print(pessoa.set_nome('joao'))


