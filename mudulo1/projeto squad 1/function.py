#//////////////////FUNÇÕES//////////////////////////
def opcoes(opcao1, opcao2, opcao3, opcao4, opcao5):
    global consulta
    print('\n', opcao1, '\n', opcao2, '\n', opcao3, '\n', opcao4, '\n', opcao5)

    consulta = str(input('\nDigite um número: ')) 
    
    if consulta not in '12345':                               
        print('ERRO! Número inválido, tente novamente entre 1 a 4')
        
    return consulta


def saida_valta():
    global duvida, consulta, voltar_inicio
    while True:    

        print('\n 1_ Voltar\n 2_ Voltar ao início \n 3_ Sair')

        saida = str(input('\nDigite um número: ')) 
        if saida == '1':                          
            break
        elif saida == '2':  
            voltar_inicio = True
            return voltar_inicio
        elif saida == '3':
            duvida = '4'
            return duvida

