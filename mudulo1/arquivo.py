# nota1 = float(input('Nota 1: '))
# nota2 = float(input('Nota 2: '))
# nota3 = float(input('Nota 3: '))
# me = (nota1 + nota2 + nota3)/3
# ma = (nota1 + nota2*2 + nota3*3+me)/7

# if ma > 9:
#     conceito = 'A'
# if ma >= 7.5 and ma < 9:
#     conceito = 'B'
# if ma > 6 and ma < 7:
#     conceito = 'C'
# if ma > 4 and ma < 6:
#     conceito = 'D'
# if ma < 4:
#     conceito = 'E'

# if ma >= 6 and ma <= 9:
#     print(f'\nAprovado, \nConceito: {conceito} \nMédia { ma:.1f}')
# elif ma < 6:
#     print(f'\n2Reprovado, \nConceito: {conceito} \nMédia { ma:.1f}')

# nome = 'jaymerson'
# for i in len(nome):
#     print(nome[::-1][i])


# sentenca = 'Está é uma string'

#replace
#print(sentenca.replace(' ', '*'))

#lower
#print(sentenca.lower())

#upper
#print(sentenca.upper())

#find
# indice = sentenca.find('uma')
# print(indice)


# sentença = 'X-DSPAM-Confidence:0.8475'
# indice = sentença.find(':')
# # print(indice)
# num = sentença[indice+1:]
# print(float(num) * 100)

while True:                                         
    print('[ 1 ] Dúvidas sobre codewars\n'
          '[ 2 ] Dúvidas sobre discord\n'
          '[ 3 ] Dúvidas sobre as aulas\n'
          '[ 4 ] Sair')

    assunto = input('Digite um número: ')[0]        
    if assunto == '4':              
        break
    if assunto not in '1234':        
        print('ERRO! Número invalido, tente novamente!')

    if assunto == '1':              
        while True:                 
            print('[ 1 ] link de acesso?\n'
                  '[ 2 ] Pontuação esperada?\n'
                  '[ 3 ] Quais tecnologias treinar?\n'
                  '[ 4 ] Retornar ao início')

            pergunta = input('Digite um número: ')[0]       
            if pergunta == '4':                             
                break
            if pergunta not in '1234':                      
                print('ERRO! Número invalido, tente novamente!')

            if int(pergunta) == 1:                          
                print('Link de acesso do Qualified é: https://codewars.com')
            elif int(pergunta) == 2:                        
                print('Assunto 1, pergunta 1, resposta 2')
            elif int(pergunta) == 3:                       
                print('Assunto 1, pergunta 1, resposta 3') 

            elif pergunta == '2':                           
                while True:                                 
                    print('[ 1 ] Assunto 1, pergunta 2\n'
                          '[ 2 ] Assunto 1, pergunta 2\n'
                          '[ 3 ] Assunto 1, pergunta 2\n'
                          '[ 4 ] Retornar ao início')

                    pergunta = input('Digite um número: ')[0]       
                    if pergunta == '4':                            
                        pergunta = ''                               
                        break
                    if pergunta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(pergunta) == 1:      
                        print('Assunto 1, pergunta 2, resposta 1')
                    elif int(pergunta) == 2:    
                        print('Assunto 1, pergunta 2, resposta 2')
                    elif int(pergunta) == 3:    
                        print('Assunto 1, pergunta 2, resposta 3')

            elif pergunta == '3':               
                while True:                     
                    print('[ 1 ] Assunto 1, pergunta 3\n'
                          '[ 2 ] Assunto 1, pergunta 3\n'
                          '[ 3 ] Assunto 1, pergunta 3\n'
                          '[ 4 ] Retornar ao início')

                    pergunta = input('Digite um número: ')[0]       
                    if pergunta == '4':                 
                        pergunta = ''                   
                        break
                    if pergunta not in '1234':          
                        print('ERRO! Número invalido, tente novamente!')

                    if int(pergunta) == 1:             
                        print('Assunto 1, pergunta 3, resposta 1')
                    elif int(pergunta) == 2:            
                        print('Assunto 1, pergunta 3, resposta 2')
                    elif int(pergunta) == 3:                               
                        print('Assunto 1, pergunta 3, resposta 3')
    
    elif assunto == '2':
        while True:
            print('[ 1 ] Assunto 2, pergunta 1\n'
                  '[ 2 ] Assunto 2, pergunta 2\n'
                  '[ 3 ] Assunto 2, pergunta 3\n'
                  '[ 4 ] Retornar ao início')
            
            pergunta = input('Digite um número: ')[0]
            if pergunta == '4':
                pergunta = ''
                break
            if pergunta not in '1234':
                print('ERRO! Número invalido, tente novamente!')

            if pergunta == '1':
                pergunta = input('Digite um número: ')[0]
                if pergunta == '4':
                    pergunta = ''
                    break
                if pergunta not in '1234':
                    print('ERRO! Número invalido, tente novamente!')

                if int(pergunta) == 1:
                    print('Assunto 2, pergunta 1, resposta 1')
                elif int(pergunta) == 2:
                    print('Assunto 2, pergunta 1, resposta 2')
                elif int(pergunta) == 3:
                    print('Assunto 2, pergunta 1, resposta 3')

            if pergunta == '2':
                while True:
                    print('[ 1 ] Assunto 2, pergunta 2\n'
                          '[ 2 ] Assunto 2, pergunta 2\n'
                          '[ 3 ] Assunto 2, pergunta 2\n'
                          '[ 4 ] Sair')

                    pergunta = input('Digite um número: ')[0]
                    if pergunta == '4':
                        pergunta = ''
                        break
                    if pergunta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(pergunta) == 1:
                        print('Assunto 2, pergunta 2, resposta 1')
                    elif int(pergunta) == 2:
                        print('Assunto 2, pergunta 2, resposta 2')
                    elif int(pergunta) == 3:
                        print('Assunto 2, pergunta 2, resposta 3')

            if pergunta == '3':
                while True:
                    print('[ 1 ] Assunto 2, pergunta 3\n'
                          '[ 2 ] Assunto 2, pergunta 3\n'
                          '[ 3 ] Assunto 2, pergunta 3\n'
                          '[ 4 ] Sair')

                    pergunta = input('Digite um número: ')[0]
                    if pergunta == '4':
                        pergunta = ''
                        break
                    if pergunta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(pergunta) == 1:
                        print('Assunto 2, pergunta 3, resposta 1')
                    elif int(pergunta) == 2:
                        print('Assunto 2, pergunta 3, resposta 2')
                    elif int(pergunta) == 3:
                        print('Assunto 2, pergunta 3, resposta 3')
                    
    elif assunto == '3':
        while True:
            print('[ 1 ] Assunto 3\n'
                  '[ 2 ] Assunto 3\n'
                  '[ 3 ] Assunto 3\n'
                  '[ 4 ] Sair')

            pergunta = input('Digite um número: ')[0]
            if pergunta == '4':
                pergunta = ''
                break
            if pergunta not in '1234':
                print('ERRO! Número invalido, tente novamente!')

            if pergunta == '1':
                while True:
                    print('[ 1 ] Assunto 3, pergunta 1\n'
                          '[ 2 ] Assunto 3, pergunta 1\n'
                          '[ 3 ] Assunto 3, pergunta 1\n'
                          '[ 4 ] Sair')

                    pergunta = input('Digite um número: ')[0]
                    if pergunta == '4':
                        pergunta = ''
                        break
                    if pergunta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(pergunta) == 1:
                        print('Assunto 3, pergunta 1, resposta 1')
                    elif int(pergunta) == 2:
                        print('Assunto 3, pergunta 1, resposta 2')
                    elif int(pergunta) == 3:
                        print('Assunto 3, pergunta 1, resposta 3')

            if pergunta == '2':
                while True:
                    print('[ 1 ] Assunto 3, pergunta 2\n'
                          '[ 2 ] Assunto 3, pergunta 2\n'
                          '[ 3 ] Assunto 3, pergunta 2\n'
                          '[ 4 ] Sair')

                    pergunta = input('Digite um número: ')[0]
                    if pergunta == '4':
                        pergunta = ''
                        break
                    if pergunta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(pergunta) == 1:
                        print('Assunto 3, pergunta 2, resposta 1')
                    elif int(pergunta) == 2:
                        print('Assunto 3, pergunta 2, resposta 2')
                    elif int(pergunta) == 3:
                        print('Assunto 3, pergunta 2, resposta 3')

            if pergunta == '3':
                while True:
                    print('[ 1 ] Assunto 3, pergunta 3\n'
                          '[ 2 ] Assunto 3, pergunta 3\n'
                          '[ 3 ] Assunto 3, pergunta 3\n'
                          '[ 4 ] Sair')

                    pergunta = input('Digite um número: ')[0]
                    if pergunta == '4':
                        pergunta = ''
                        break
                    if pergunta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(pergunta) == 1:
                        print('Assunto 3, pergunta 3, resposta 1')
                    elif int(pergunta) == 2:
                        print('Assunto 3, pergunta 3, resposta 2')
                    elif int(pergunta) == 3:
                        print('Assunto 3, pergunta 3, resposta 3')
                    
print('Obrigado, volte sempre!!!')

