def erro1234(assunto):
    if assunto not in '1234':
        return print('ERRO! Número inválido, tente novamente entre 1 a 4!')
    
def erro12(sair):
        if sair not in '12':
            return print('ERRO! Número inválido. tente novamente, 1 ou 2!')        
                 
def print_perg(pergunta1, pergunta2, pergunta3, pergunta4):
    return print(pergunta1, pergunta2, pergunta3, pergunta4)

def informacao(resposta):
    
    print(resposta)

while True:
    
    print('\n [ 1 ] Dúvidas sobre codewars\n'
            ' [ 2 ] Dúvidas sobre discord\n'
            ' [ 3 ] Dúvidas sobre as aulas\n'
            ' [ 4 ] Sair')
    
    assunto = str(input('\nDigite um número: ')).strip()[0]     

    if assunto == '4':                              
        break
                                   
    erro1234(assunto)

    if assunto == '1':                                    
        while True: 
            if assunto == '4':
                break
            pergunta1 = '\n [ 1 ] link de acesso?\n'
            pergunta2 = '[ 2 ] Pontuação esperada?\n'
            pergunta3 = '[ 3 ] Quais tecnologias treinar?\n'
            pergunta4 = '[ 4 ] Retornar ao início'
            print_perg(pergunta1, pergunta2, pergunta3, pergunta4)
            
            pergunta = str(input('\nDigite um número: ')).strip()[0]  
            erro1234(pergunta)
            if pergunta == '4':
                break

            if pergunta == '1':
                resposta = '\nLink de acesso do Qualified é: https://codewars.coom\n'
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break

            elif pergunta == '2':                          
                resposta ='\nResposta: Assunto 1, pergunta 2'
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break

            elif pergunta == '3':                           
                resposta = '\nResposta: Assunto 1, pergunta 3' 
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break

    elif assunto == '2':                                    
        while True:                                         

            if assunto == '4':
                break

            if assunto == '4':                              
                    break 
            pergunta1 = '\n[ 1 ] Assunto 2, pergunta 1\n'
            pergunta2 = '[ 2 ] Assunto 2, pergunta 2\n'
            pergunta3 = '[ 3 ] Assunto 2, pergunta 3\n'
            pergunta4 = '[ 4 ] Retornar ao início'
            print_perg(pergunta1, pergunta2, pergunta3, pergunta4)
            
            pergunta = str(input('\nDigite um número: ')).strip()[0]

            if pergunta == '4':                             
                break
                 
            erro1234(pergunta)

            if pergunta == '1':                              
                resposta =  '\nResposta: Assunto 2, pergunta 1'
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break

            elif pergunta == '2':                           
                resposta = '\nResposta: Assunto 2, pergunta 2'
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break

            elif pergunta == '3':                           
                resposta = '\nResposta: Assunto 2, pergunta 3'
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break    

    elif assunto == '3':                                    
        while True:  

            if assunto == '4':                              
                    break 
            
            pergunta1 = '\n[ 1 ] Assunto 3, pergunta 1\n'
            pergunta2 = '[ 2 ] Assunto 3, pergunta 2\n'
            pergunta3 = '[ 3 ] Assunto 3, pergunta 3\n'
            pergunta4 = '[ 4 ] Retornar ao início'
            print_perg(pergunta1, pergunta2, pergunta3, pergunta4)
            
            pergunta = input('\nDigite um número: ')[0]
          
            erro1234(pergunta)

            if pergunta == '1':                             
                print('\nResposta: Assunto 3, pergunta 1')
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break

            elif pergunta == '2':                          
                resposta = '\nResposta: Assunto 3, pergunta 2'
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break

            elif pergunta == '3':                           
                resposta = '\nResposta: Assunto 3, pergunta 3'
                informacao(resposta)
                while True:
                    print('\n[ 1 ] Sair do programa\n'
                            '[ 2 ] Voltar')
                    
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    erro12(sair)

                    if sair == '1': 
                        assunto = '4'
                        break 
                    elif sair == '2':
                        break
                    
print('\nFim do programa!\n')                                      

                    




















#            variavel01     variavel02
# def meu_nome(idade,          nome):
#     return print(nome, idade)   

        


# variavel01 = 'jayme'                              
# variavel02 = 24

# meu_nome(variavel01, variavel02)                       
















# def linha(argumento1, argumento2):                                                            
#     return print(argumento1,argumento2)      

# lin = '=================================='
# a = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' 

# linha(lin, a)                     
# linha(lin, a)
# linha(lin, a)

