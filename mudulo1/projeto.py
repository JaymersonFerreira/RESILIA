while True:                                                 #enquanto for verdade repita
    print('\n[ 1 ] Dúvidas sobre codewars\n'
          '[ 2 ] Dúvidas sobre discord\n'
          '[ 3 ] Dúvidas sobre as aulas\n'
          '[ 4 ] Sair')
    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na variavel 'assunto'
    assunto = str(input('\nDigite um número: ')).strip()[0]     

    if assunto not in '1234':                               #se 'assunto' não estiver dentro da string '1234' imprima ERRO!
        print('ERRO! Número inválido, tente novamente!')

    if assunto == '1':                                      #se 'assunto' for igual a '1'
        while True:                                         #enquanto for verdade repita

            if assunto == '4':                              #se 'assunto dor igual a '4' então quebra o loop da linha 1
                    break      
                     
            print('\n[ 1 ] link de acesso?\n'
                    '[ 2 ] Pontuação esperada?\n'
                    '[ 3 ] Quais tecnologias treinar?\n'
                    '[ 4 ] Retornar ao início')
            #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'pergunta'
            pergunta = str(input('\nDigite um número: ')).strip()[0]  
                 
            if pergunta == '1':                             #se 'pergunta' for igual a '1' imprima
                print('\nLink de acesso do Qualified é: https://codewars.coom\n')
                
                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver em '12' imprima ERRO!
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confira se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 13
                        break
                    elif sair == '2':                       #se não confira se 'sair' é igual a '2' então e quebra o loop da linha 28
                        break

            elif pergunta == '2':                           #se 'pergunta' for igual a '2' imprima
                print('\nResposta: Assunto 1, pergunta 2')

                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver em '12' imprima ERRO!
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confira se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 13
                        break
                    elif sair == '2':                       #se não confira se 'sair' é igual a '2' então e quebra o loop da linha 45
                        break

            elif pergunta == '3':                           #se 'pergunta' for igual a '3' imprima
                print('\nResposta: Assunto 1, pergunta 3') 
                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver em '12' imprima ERRO!
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confira se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 13
                        break
                    elif sair == '2':                       #se não confira se 'sair' é igual a '2' então e quebra o loop da linha 61
                        break
                
    elif assunto == '2':                                    #se 'assunto' for igual a '2' então
        while True:                                         #enquanto for verdade repita

            if assunto == '4':                              #se 'assunto' for igual a '4' então quebra o loop da linha 1
                    break 
            
            print('\n[ 1 ] Assunto 2, pergunta 1\n'
                  '[ 2 ] Assunto 2, pergunta 2\n'
                  '[ 3 ] Assunto 2, pergunta 3\n'
                  '[ 4 ] Retornar ao início')
            #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'pergunta'
            pergunta = str(input('\nDigite um número: ')).strip()[0]

            if pergunta == '4':                             #se 'pergunta' for igual a '4' então
                break

            if pergunta not in '1234':                      #se 'pergunta' não estiver em '1234' imprima ERRO!
                print('ERRO! Número inválido, tente novamente!')

            if pergunta == '1':                             #se 'pergunta' for igual a '1' então imprima a Resposta
                print('\nResposta: Assunto 2, pergunta 1')

                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver em '12' imprima ERRO!
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confira se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 76
                        break
                    elif sair == '2':                       #se não confira se 'sair' é igual a '2' então e quebra o loop da linha 97
                        break

            elif pergunta == '2':                           #se não confere se 'perfunta' é igual a '2' então imprima a Resposta
                print('\nResposta: Assunto 2, pergunta 2')
                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver em '12' imprima ERRO!
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confira se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 76
                        break
                    elif sair == '2':                       #se não confira se 'sair' é igual a '2' então e quebra o loop da linha 113
                        break

            elif pergunta == '3':                           #se não confere se 'perfunta' é igual a '3' então imprima a Resposta
                print('\nResposta: Assunto 2, pergunta 3')
                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver em '12' imprima ERRO!
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confira se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 76
                        break
                    elif sair == '2':                       #se não confira se 'sair' é igual a '2' então e quebra o loop da linha 129
                        break     

    elif assunto == '3':                                    #se não confere se pergunra é igual a '3'
        while True:                                         #enquanto for verdade repita

            if assunto == '4':                              #se 'assunto' for igual a '4' então quebra o loop da linha 1
                    break 
            
            print('\n[ 1 ] Assunto 3, pergunta 1\n'
                  '[ 2 ] Assunto 3, pergunta 2\n'
                  '[ 3 ] Assunto 3, pergunta 3\n'
                  '[ 4 ] Retornar ao início')
            #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'pergunta'
            pergunta = input('\nDigite um número: ')[0]

            if pergunta == '4':                             #se 'pergunta' for igual a '4'
                break
            if pergunta not in '1234':                      #se 'sair' não estiver em '1234' imprima ERRO!
                print('ERRO! Número inválido, tente novamente!')

            if pergunta == '1':                             #se 'pergunta' for igual a '1'
                print('\nResposta: Assunto 3, pergunta 1')

                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver na string '12'
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confere se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 144
                        break
                    elif sair == '2':                       #se não confere se 'sair' é igual a '2' então quebra o loop da linha 164
                        break

            elif pergunta == '2':                           #se não confere se pergunra é igual a '3'
                print('\nResposta: Assunto 3, pergunta 2')

                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver em '12' imprima ERRO!
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confira se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 144
                        break
                    elif sair == '2':                       #se não confira se 'sair' é igual a '2' então quebra o loop da linha 181
                        break

            elif pergunta == '3':                           #se não confere se pergunra é igual a '3'
                print('\nResposta: Assunto 3, pergunta 3')

                while True:                                 #enquanto for verdade repita
                    print('\n[ 1 ] Sair\n'
                            '[ 2 ] Voltar')
                    #Pega somente o primeiro elemento da string [0], retira os espaços .strip() e atribui na vareavel 'sair'
                    sair = str(input('\nDigite um número: ')).strip()[0] 

                    if sair not in '12':                    #se 'sair' não estiver em '12' imprima ERRO!
                        print('ERRO! Número inválido, tente novamente!')
                    elif sair == '1':                       #se não confira se 'sair' é igual a '1' então
                        assunto = '4'                       #'assunto' recebe '4' e quebra o loop da linha 144
                        break
                    elif sair == '2':                       #se não confira se 'sair' é igual a '2' então quebra o loop da linha 198
                        break
                    
    if assunto == '4':                                      #se 'assunto' for igual a '4' então quebra o loop da linha 1
        break
                    
print('\nFim do programa!\n'
      'Obrigado! Volte sempre!!!')



















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

