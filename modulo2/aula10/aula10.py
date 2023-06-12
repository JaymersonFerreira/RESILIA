# class ListadeCompras():
#     lista = []

#     def inserirItens(self):
#         msg = input('Insira um item na lista ')
#         self.lista.append(msg)


#     def consultarItens(self):
#         print(self.lista)

# ListaJaneiro = ListadeCompras()

# # ListaJaneiro.inserirItens()

# # ListaJaneiro.consultarItens()

# while True:
#     print('*' * 30)
#     print('1 - Iserir nvo item')
#     print('2 - Consulta itens')
#     print('3 - Sair')
#     print('*' * 30, '\n')


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
retangulo = Retangulo(1, 1)

base = float(input('Digite a base de retangulo: '))
altura = float(input('Digite a altura de retangulo: '))
retangulo.base = base
retangulo.altura = altura
areaRetangulo = retangulo.area()
perimetroRetangulo = retangulo.perimetro()

print('area do retangulo: ', areaRetangulo)
print('perimetro do retangulo: ', perimetroRetangulo)