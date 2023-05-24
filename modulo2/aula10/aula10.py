class ListadeCompras():
    lista = []

    def inserirItens(self):
        msg = input('Insira um item na lista ')
        self.lista.append(msg)


    def consultarItens(self):
        print(self.lista)

ListaJaneiro = ListadeCompras()

# ListaJaneiro.inserirItens()

# ListaJaneiro.consultarItens()

while True:
    print('*' * 30)
    print('1 - Iserir nvo item')
    print('2 - Consulta itens')
    print('3 - Sair')
    print('*' * 30, '\n')


    