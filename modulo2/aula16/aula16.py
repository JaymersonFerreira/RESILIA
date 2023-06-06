# class Gato():
#     nome = ''

#     def __init__(self, nome):
#         self.nome = nome

#     def miar(self, nome):
#         print('O gato', nome, ' miou!')
    
# gamora = Gato('gato')
# gamora.nome = 'Gamora'
# print(gamora.nome)
# nome = input('Digite o nome do gato: ')
# gamora.miar(nome)



class Funcionario:
    def __init__(self, nome, salarioBase):
        self.nome = nome
        self.salarioBase = salarioBase

    def calcularSalario(self):
        pass


class FuncionarioClt(Funcionario):
    def __init__(self, nome, salarioBase, experiencia):
        Funcionario.__init__(self, nome, salarioBase)
        self.experiencia = experiencia

class FuncionarioPJ(Funcionario):
    def __init__(self, nome, salarioBase, experiencia):
        Funcionario.__init__(self, nome, salarioBase)
        self.experiencia = experiencia
    
    def calcularSalario(self):
        return self.salarioBase * self.experiencia
    
