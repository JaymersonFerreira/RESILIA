#//////////////////FUNÇÕES//////////////////////////
def intro_duvida(opcao1, opcao2, opcao3, opcao4):
    global duvida, voltar_inicio
    duvida = None
    voltar_inicio = False
    print('\n', opcao1, '\n', opcao2, '\n', opcao3, '\n', opcao4)
    duvida = str(input('\nDigite um número: ')) 
    if duvida not in '1234':                               
        print('ERRO! Número inválido, tente novamente entre 1 a 4')
    return duvida, voltar_inicio


def intro_consulta(opcao1, opcao2, opcao3, opcao4, opcao5):
    global consulta
    print('\n', opcao1, '\n', opcao2, '\n', opcao3, '\n', opcao4,'\n', opcao5)
    consulta = str(input('\nDigite um número: ')) 
    if consulta not in '12345':                               
        print('ERRO! Número inválido, tente novamente entre 1 a 4')   
    return consulta


def saida_valta():
    global duvida, voltar_inicio
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


#////////////////////PRINCIPAL///////////////////////
duvida = None
consulta = None
voltar_inicio = False
while True:
    if duvida == '4' or consulta == '5':       
        break   

    opcao1 = '1_ Dúvidas sobre Codewars'
    opcao2 = '2_ Dúvidas sobre Discord'
    opcao3 = '3_ Dúvidas sobre as aulas'
    opcao4 = '4_ Sair'
    intro_duvida(opcao1, opcao2, opcao3, opcao4)

    if duvida == '4' or consulta == '5':
        break
    elif duvida == '1':                                      
        while True:                                     
            if duvida == '4' or voltar_inicio == True:                              
                break

            opcao1 = '1_ link de acesso?'
            opcao2 = '2_ Classificação?'
            opcao3 = '3_ Quais tecnologias treinar?'
            opcao4 = '4_ Voltar ao início'
            opcao5 = '5_ Sair'
            intro_consulta(opcao1, opcao2, opcao3, opcao4, opcao5)
            if consulta == '4' or consulta == '5':
                break
                #RESPOSTA       
            elif consulta == '1':
                print('Link de acesso do Qualified é: https://codewars.com')
                saida_valta()
                #RESPOSTA     
            elif consulta == '2':
                print('As classificações são usadas para indicar a proficiência dos usuários e a dificuldade do Kata. Existem duas classes de ranks, Kyu e Dan, que são divididas em 8 níveis cada.')
                saida_valta()
                #RESPOSTA
            elif consulta == '3':
                print('Linguagem de programação que podem ser praticadas no Codewars são: C, C#, C++, Dart, Go, Haskell, Java, JavaScript, Kotlin, Lua, PHP, Python, R, Ruby, Rust, SQL, Scala, Solidity, Swift e TypeScript') 
                saida_valta()

    elif duvida == '2':                                    
        while True:                                         
            if duvida == '4' or voltar_inicio == True:                              
                break 
            opcao1 = '1_ O que é o Discord?'
            opcao2 = '2_ Por que utilizaremos o Discord?'
            opcao3 = '3_ Link de acesso?'
            opcao4 = '4_ Voltar ao início'
            opcao5 = '5_ Sair'
            intro_consulta(opcao1, opcao2, opcao3, opcao4, opcao5) 
            if consulta == '4' or consulta == '5':
                break
                #RESPOSTA
            elif consulta == '1':       
                print('O Discord é um aplicativo que ajuda na interação da comunidade, todos nós podemos conversar por lá, enviar comunicados e solicitar suporte.')
                saida_valta()
                #RESPOSTA
            elif consulta == '2':       
                print('\nPorque seŕa pelo nosso servidor no Discord que a Turma poderá interagir com bate-papo, dúvidas,    dicas e ajuda. \nTambém por meio da plataforma que a turma receberá os comunicados oficiais.')
                saida_valta()
                #RESPOSTA
            elif consulta == '3':       
                print('Link do nosso servido no Discord: https://discord.gg/eX8YrvT3')
                saida_valta()
    
    elif duvida == '3':                                    
        while True:                                         
            if duvida == '4' or voltar_inicio == True:                              
                break 
            opcao1 = '1_ Acesso ás aulas?'
            opcao2 = '2_ Link do Portal do aluno?'
            opcao3 = '3_ Dias e horarios?'
            opcao4 = '4_ Voltar ao início'
            opcao5 = '5_ Sair'
            intro_consulta(opcao1, opcao2, opcao3, opcao4, opcao5) 
            if consulta == '4' or consulta == '5':
                break
                #RESPOSTA    
            elif consulta == '1':  
                print('O acesso é a partir do portal do aluno! Lembre-se de entrar no Portal 10 minutinhos antes do início da aula para garantir que tudo esteja certo.')
                saida_valta()
                #RESPOSTA
            elif consulta == '2':       
                print('Link do Portal do aluno: https://aluno.resilia.work/')
                saida_valta()
                #RESPOSTA
            elif consulta == '3':       
                print('Os dias das aulas são de segunda a quinta-sexta das 15h as 18h')
                saida_valta()

print('\nFim do programa!'
      '\nObrigado! Volte sempre!!!')
