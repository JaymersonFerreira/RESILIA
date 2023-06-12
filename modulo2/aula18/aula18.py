#fila

# fila = [10, 20, 30, 40, 50]
# fila.append(60)
# print('fila.append(60): ',fila)
# fila.pop(0)
# print('fila.pop(0): ',fila)
# fila.append(70)
# print('fila.append(70): ',fila)
# fila.pop(0)
# print('fila.pop(0): ',fila)

class Questionario():
    def __init__(self):
        self.valores = []
    
    def consultaItens(self):
        return print(self.valores)
    
    def inserirItens(self):
        msg = input('Iserir um novo itenm na lista: ')
        self.valores.append(msg)

while True:
    print('*'*30)
    print('')
    print()
    print()
    print()
    print()