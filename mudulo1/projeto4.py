#erro se nao digita entre 1 a 4
def erro1234(duvida):
    if duvida not in '1234':
        print('ERRO! Número inválido, tente novamente entre 1 a 4!')
    

#erro se nao digita 1 ou 2  
def erro12(sair):
        if sair not in '12':
            print('ERRO! Número inválido. tente novamente, 1 ou 2!')
              

#print das consultas                 
def print_consulta(consulta1, consulta2, consulta3, consulta4):   
    print(consulta1, consulta2, consulta3, consulta4)


#imprime a resposta e consulta se quer sair
def informacao(resposta):
    
    #imprime a resposta
    print(resposta)
    while True:
        #pucha a variavel do escopo global
        global duvida    

        print(' \n[ 1 ] Sair do programa'
              ' \n[ 2 ] Voltar')

        sair = str(input('\nDigite um número: ')) 

        erro12(sair)        

        if sair == '1': 
            duvida = '4'    #Altera a 'duvida' para '4' fazendo quebrar o loop da linha 39
            break 
        elif sair == '2':   #Se sair for igual a '2' então quebra o loop da linha 23
            break


# def con
duvida = ''
while True:
    if duvida == '4':      #quebra a o lopp da linha 42
        break

    print(' \n[ 1 ] Dúvidas sobre codewars'
          ' \n[ 2 ] Dúvidas sobre discord'
          ' \n[ 3 ] Dúvidas sobre as aulas'
          ' \n[ 4 ] Sair')
    
    duvida = str(input('\nQual é a sua dúvida? '))
    
    if duvida == '4':      #quebra o loop da linha 41
        break       
      
    erro1234(duvida)       #confere se o valor de 'duvida' estar entre '1' a '4'

    if duvida == '1':                                    
        while True: 

            if duvida == '4':
                break

            consulta1 = ' \n[ 1 ] link de acesso?'
            consulta2 = ' \n[ 2 ] Pontuação esperada?'
            consulta3 = ' \n[ 3 ] Quais tecnologias treinar?'
            consulta4 = ' \n[ 4 ] Retornar ao início'

            print_consulta(consulta1, consulta2, consulta3, consulta4)
            
            consulta = str(input('\nO que deseja consultar? '))  

            erro1234(consulta)

            if consulta == '4':
                break

            elif consulta == '1':

                resposta = '\nLink de acesso do Qualified é: https://codewars.coom\n'
                informacao(resposta)                

            elif consulta == '2': 

                resposta ='\nResposta: duvida 1, consulta 2'
                informacao(resposta)
                
            elif consulta == '3':                           
                resposta = '\nResposta: duvida 1, consulta 3' 
                informacao(resposta)
                
    elif duvida == '2':                                    
        while True:                                         

            if duvida == '4':
                break

            consulta1 = ' \n[ 1 ] duvida 2, consulta 1'
            consulta2 = ' \n[ 2 ] duvida 2, consulta 2'
            consulta3 = ' \n[ 3 ] duvida 2, consulta 3'
            consulta4 = ' \n[ 4 ] Retornar ao início'

            print_consulta(consulta1, consulta2, consulta3, consulta4)
            
            consulta = str(input('\nDigite um número: '))

            if consulta == '4':                             
                break
                 
            erro1234(consulta)

            if consulta == '1':                              
                resposta =  '\nResposta: duvida 2, consulta 1'
                informacao(resposta)
                
            elif consulta == '2':                           
                resposta = '\nResposta: duvida 2, consulta 2'
                informacao(resposta)
                
            elif consulta == '3':                           
                resposta = '\nResposta: duvida 2, consulta 3'
                informacao(resposta)
                    
    elif duvida == '3':                                    
        while True:  

            if duvida == '4':                              
                    break 
            
            consulta1 = ' \n[ 1 ] duvida 3, consulta 1'
            consulta2 = ' \n[ 2 ] duvida 3, consulta 2'
            consulta3 = ' \n[ 3 ] duvida 3, consulta 3'
            consulta4 = ' \n[ 4 ] Retornar ao início'
            print_consulta(consulta1, consulta2, consulta3, consulta4)
            
            consulta = input('\nDigite um número: ')[0]

            if consulta == '4':
                break

            erro1234(consulta)

            if consulta == '1':                             
                resposta = '\nResposta: duvida 3, consulta 1'
                informacao(resposta)
                
            elif consulta == '2':                          
                resposta = '\nResposta: duvida 3, consulta 2'
                informacao(resposta)
                
            elif consulta == '3':                           
                resposta = '\nResposta: duvida 3, consulta 3'
                informacao(resposta)
                                    
print('\nFim do programa!\n')                                      

                    




















#         #    variavel01     variavel02
# def meu_nome(idade,          nome):
#     return print(nome, idade)   

        


# variavel01 = 'jayme'                              
# variavel02 = 24

# meu_nome(variavel01, variavel02)                       
















# def linha():
#     return print('==================================')      


# linha()                     
# linha()
# linha()

