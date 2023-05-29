# class Lampada():
    
#     #atributo
#     cor = 'amarela'
#     acesa = False
    
#     #método
#     def acender(self):
#         self.acesa = self.acesa = True
            


# lampada = Lampada()
# print(lampada.acesa)
# lampada.acender()
# print(lampada.acesa)
lista = []
class Carro:
    cor = 'amarela'
    def __init__(self, rodas, capacidadeTanque):
        self.rodas = rodas
        self.qtdLitrosTanque = capacidadeTanque

    def get_cor(self):
        return self.cor
    
    def set_cor(self, novaCor):
        self.cor = novaCor

amelie = Carro(4, 50)
# lista.append(amelie.rodas)
# lista.append(amelie.qtdLitrosTanque)
# lista.append(amelie.get_cor())
# print(f'Rodas: {lista[0]:>15}')
# print(f'Tanque: {lista[1]:>15}')
# print(f'Cor: {lista[2]:>15}')

print(amelie.get_cor())
amelie.set_cor('azul')
print(amelie.get_cor())

