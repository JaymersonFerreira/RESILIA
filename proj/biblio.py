voltar_inicio = False
consulta = ''
duvida = ''

def intro_duvida(opcoes):
    while True:
        print(*opcoes, sep='\n')
        duvida = input('\nDigite um número: ').strip()[0]
        if duvida not in ['1', '2', '3', '4']:
            print('ERRO! Número inválido, tente novamente entre 1 a 4')
        else:
            return duvida

def intro_consulta(opcoes):
    while True:
        print(*opcoes, sep='\n')
        consulta = input('\nDigite um número: ').strip()[0]
        if consulta not in ['1', '2', '3', '4', '5']:
            print('ERRO! Número inválido, tente novamente entre 1 a 5')
        else:
            return consulta

def saida_volta():
    global duvida
    while True:
        print('\n 1_ Voltar\n 2_ Voltar ao início \n 3_ Sair')
        saida = input('\nDigite um número: ').strip()[0]
        if saida == '1':
            break
        elif saida == '2':
            return True
        elif saida == '3':
            duvida = '4'
            return duvida


def boas_vindas():
    print('\nBem vindo á AllFor Games, o melhor canal de jogos do mundo. Como posso de chamar?')
    nome = input('Nome: ').upper()
    print('-'*80)
    print('\nNo que posso te ajudar ' + nome + '?')