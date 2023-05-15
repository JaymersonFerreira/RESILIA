# def insereNaFila(fila, elemento):
#     return fila.append(elemento)


# def retiraNaFila(fila):
#     if len(fila):
#         return fila.pop(0)


# def tamanho(fila):
#     tam = len(fila)
#     if len(fila) == 0:
#         print('Lista vazia!')
#     else:
#         print(fila)
#         print('A fila tem',tam)


# fila = []
# for i in range(8):
#     insereNaFila(fila, i)

# retiraNaFila(fila)
# tamanho(fila)


#////////função//////////////////////////
def insereNaPilha(pilha, elemento):
    return pilha.append(elemento)

def tamanho(pilha):
    global tam
    tam = len(pilha)
    return tam

def verifica_tamanho(tam):
    if tam == 0:
        print('Lista vazia!')
    else:
        print('A pilha tem',tam)


#//////////principal/////////////////////
tam = ''
pilha = []
for i in range(8):
    insereNaPilha(pilha, i)

print(pilha)
tamanho(pilha)
verifica_tamanho(tam)

