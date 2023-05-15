import function

#Neste arquivo está contido a estrutura di chatbot com inputs do usuario e saídas de respostas.

usuario = input('Olá. Como posso te chamar? ').upper().strip()

#AQUI DÁ AS BOAS VINDAS E PERGUNTA SE O USUÁRIO QUER PROSSEGUIR OU NÃO.
print(function.boasVindas(usuario))


#ESSE LOOP DÁ AS OPÇÕES INICIAIS AO USUÁRIO. ONDE TUDO COMEÇA.
while True:
    resposta_inicial = input('\n')
    if resposta_inicial.lower().strip() in ['sim' , 's']:
        print(function.menu1(usuario))
        break
    elif resposta_inicial.lower() in ['não' , 'nao' , 'n']:
        print(function.encerra_atendimento(usuario))
        break
    else:
        print(function.option_error())
        

#APOS O USUÁRIO SAIR DAS OPÇÕES INICIAIS, ENTRA NESSE LOOP
while True:
    #ESTE PRIMEIRO LOOP DIRECIONA O USUARIO PARA AS OPÇÕES PARA OS MENUS SEGUINTES
    resposta_secundaria = input('\n')
    #CASO O USUÁRIO ESCOLHA O MENU 1_1 ENTRARÁ NESSA CONDIÇÃO PARA ENVIO DA FATURA
    if resposta_secundaria == '1':
        print(function.menu_1_1())
        while True:
            resposta1 = input('\n')
            #ENVIO DA FATURA POR EMAIL
            if resposta1 == '1':
                print('\nDigite abaixo seu email para envio da 2ª via:')
                resposta1_1 = input('')
                print(function.tempo())
                print(f'\nENVIADO Sr(a){usuario}. Verifique seu email na caixa de entrada, span e lixeira. Sua fatura já foi enviada.')
                print(function.algo_mais())
                resposta1_2 = input('')
                if resposta1_2.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta1_2.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #ENVIO DA FATURA POR WHATSAPP
            elif resposta1 == '2':
                print('\nDigite abaixo o numero corresponte ao seu WhatsApp para o envio da 2ª Via:')
                resposta1_3 = input('')
                print(function.tempo())
                print(f'\nENVIADO Sr(a){usuario}. Verifique seu WhatsApp. Caso não chegue de imediato aguarde alguns minutos antes de tentar novamente.')
                print(function.algo_mais())
                resposta1_4= input('')
                if resposta1_4.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta1_4.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #ENVIO DA FATURA SMS (APENAS CÓDIGO DE BARRAS)
            elif resposta1 == '3':
                print('\nDigite abaixo o numero telefônico que deseja receber a 2ª Via:')
                resposta1_5 = input('')
                print(function.tempo())
                print(f'\nENVIADO Sr(a){usuario}. Verifique as mensagens SMS em seu celular. Caso não receba de imediato aguarde alguns minutos antes de tentar novamente.')
                print(function.algo_mais())
                resposta1_6 = input('')
                if resposta1_6.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta1_6.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            elif resposta1 == '4':
                print(function.encerra_atendimento(usuario))
                break
            else:
                print(function.option_error())
    #CASO O USUÁRIO ESCOLHA O MENU 1_2 ENTRARÁ NESSA CONDIÇÃO PARA FALTA DE ENERGIA
    elif resposta_secundaria == '2':
        print(function.menu_1_2())
        while True:
            resposta2 = input('\n')
            #FALTA DE ENERGIA EM TODO O BAIRRO DO USUÁRIO
            if resposta2 == '1':
                print(f'\nOk Sr(a){usuario}. Me conta qual o nome do seu bairro:')
                resposta2_1 = input('\n').upper()
                print(function.localizar())
                print(f'Tudo certo Sr(a){usuario}. Já registrei a ocorrência para que uma equipe dirija-se ao bairro {resposta2_1}.')
                print(function.algo_mais())
                resposta2_2 = input('\n')
                if resposta2_2.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta2_2.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #FALTA DE ENERGIA APENAS NA RUA DO USUÁRIO
            elif resposta2 == '2':
                print(f'\nOk Sr(a){usuario}. Me conta qual o nome da sua rua:')
                resposta2_3 = input('\n').upper()
                print(f'\nE qual o nome do bairro:')
                resposta2_4 = input('\n').upper()
                print(function.localizar())
                print(f'Tudo certo Sr(a){usuario}. Já registrei a ocorrência para que uma equipe dirija-se á rua {resposta2_3} no bairro {resposta2_4}.')
                print(function.algo_mais())
                resposta2_5 = input('\n')
                if resposta2_5.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta2_5.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #FALTA DE ENERGIA APENAS NA CASA DO USUÁRIO
            elif resposta2 == '3':
                print(f'\nOk Sr(a){usuario}. Preciso saber de algumas informações para registrar o protocolo e enviar uma equipe técnica.')
                resposta2_6 = input('\nMe conta por favor qual o nome da rua: ').upper()
                resposta2_7 = input('Agora me fala qual o numero da casa: ')
                resposta2_8 = input('E qual o nome do bairro para finalizarmos: ').upper()
                print(function.localizar())
                print(f'\nTudo certo Sr(a){usuario}. Já registrei a ocorrência para que uma equipe dirija-se ao endereço: {resposta2_6} {resposta2_7} no bairro {resposta2_8}.')
                print(function.algo_mais())
                resposta2_9 = input('')
                if resposta2_9.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta2_9.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #VOLTAR AO MENU ANTERIOR
            elif resposta2 == '4':
                print(function.menu1(usuario))
                break
            #ENCERRAR ATENDIMENTO
            elif resposta2 == '5':
                print(function.encerra_atendimento(usuario))
                break
            #OPÇÃO INCORRETA
            else:
                print(function.option_error())
    #CASO O USUÁRIO ESCOLHA O MENU 1_3 ENTRARÁ NESSA CONDIÇAÕ PARA RELIGAÇÃO
    elif resposta_secundaria == '3':
        print(function.menu_1_3())
        while True:
            resposta3 = input('\n')
            #RELIGAÇÃO PARA O MESMO TITULAR
            if resposta3 == '1':
                print(f'\nEntendi Sr(a){usuario}. A religação é para sua titularidade. Digita abaixo por gentileza o seu CPF (APENAS NUMEROS):')
                resposta3_1 = input('\n')
                print(function.localizar_titular())
                print('\nJá encontrei aqui as informações de que preciso e registrei o protocolo para que um analista entre em contato para validar as informações para religação.')
                print(function.algo_mais())
                resposta3_2 = input('')
                if resposta3_2.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta3_2.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #RELIGAÇÃO PARA OUTRO TITULAR
            elif resposta3 == '2':
                print(f'\nEntendi Sr(a){usuario}. A religação é para outra titularidade. Digita abaixo por gentileza o seu CPF (APENAS NUMEROS):\nda pessoa que deseja e numero telefonico da mesma para entrarmos em contato.')
                print('Por motivos de segurança só abrimos protocolo de religação com a solicitação do titular.')
                resposta3_4 = input('\n')
                print(function.localizar_titular())
                print('\nJá encontrei aqui as informações de que preciso e registrei o protocolo para que um analista entre em contato para validar as informações para religação.')
                print(function.algo_mais())
                resposta3_5 = input('')
                if resposta3_5.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta3_5.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #RELIGAÇÃO PARA EMPRESAS
            elif resposta3 == '3':
                print(f'\nEntendi Sr(a){usuario}. A religação é para uma empresa. Nesse caso vou precisar de algumas informações obrigatórias, ok?')
                resposta3_6 = input('Por gentileza digite abaixo o CNPJ da empresa solicitante: ')
                resposta3_7 = input('Agora digite a razão social da empresa solicitante: ')
                resposta3_8 = input('Preciso saber agora o CPF do responsável legal da empresa supracitada: ')
                resposta3_9 = input('E para finalizar o numero telefônico do responsável: ')
                print(function.localizar_titular())
                print('\nInformações registradas e agora só aguardar que um analista entre em contato para validar as informações para religação.')
                print(function.algo_mais())
                resposta3_10 = input('')
                if resposta3_10.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta3_10.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #VOLTAR AO MENU ANTERIOR
            elif resposta3 == '4':
                print(function.menu1(usuario))
                break
            #ENCERRAR ATENDIMENTO
            elif resposta3 == '5':
                print(function.encerra_atendimento(usuario))
                break
            #OPÇÃO INCORRETA
            else:
                print(function.option_error())
    #CASO O USUÁRIO ESCOLHA O MENU 1_4 ENTRARÁ NESSA CONDIÇÃO PARA INFORMAÇÕES SOBRE A EMPRESA
    elif resposta_secundaria == '4':
        print(function.menu_1_4())
        while True:
            resposta4 = input('\n')
            #ÁREA 'SOBRE NÓS' DA EMPRESA
            if resposta4 == '1':
                print(f'\nTudo bem Sr(a){usuario}. Vi que deseja saber um pouco mais sobre nós.\n')
                print(function.sobre_nos())
                print('\nDeseja voltar ao menu anterior?')
                resposta4_1 = input('\n')
                if resposta4_1.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta4_1.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #CLIENTES E FORNECEDORES
            elif resposta4 == '2':
                print(f'\nTudo bem Sr(a){usuario}. Vi que deseja informações sobre nossos clientes e fornecedores.')
                print('Para isso, o senhor terá que acessar nosso site oficial e fazer login com CPF para ter acesso ás informações.')
                print('Nosso site é: https://energy.org')
                print('\nDeseja voltar ao menu anterior?')
                resposta4_2 = input('\n')
                if resposta4_2.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta4_2.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #SUSTENTABILIDADE
            elif resposta4 == '3':
                print(f'\nTudo bem Sr(a){usuario}. Vi que deseja informações sobre como nos preocupamos com o meio ambiente.')
                print('Para isso, recomendo acessar nosso artigo em nosso site com todas as informações de como cuidamos e criamos formas de preservar o meio ambiente.')
                print('Acesse agora: https://energy.org/article-sustentabilidade')
                print('\nDeseja voltar ao menu anterior?')
                resposta4_3 = input('\n')
                if resposta4_3.lower() in ['sim' , 's']:
                    print(function.menu1(usuario))
                    break
                elif resposta4_3.lower() in ['não' , 'nao' , 'n']:
                    print(function.encerra_atendimento(usuario))
                    break
                else:
                    print(function.option_error())
            #VOLTAR AO MENU ANTERIOR
            elif resposta4 == '4':
                print(function.menu1(usuario))
                break
            #ENCERRAR ATENDIMENTO
            elif resposta4 == '5':
                print(function.encerra_atendimento(usuario))
                break
            #MENSAGEM DE ERRO PARA DIGITAÇÃO DE CARACTERES INVÁLIDOS
            else:
                print(function.option_error())
    #CASO O USUÁRIO OPTE POR NÃO CONTINUAR O ATENDIMENTO ENTRARÁ NESSA CONDIÇÃO DE ENCERRAMENTO
    elif resposta_secundaria == '5':
        print(function.encerra_atendimento(usuario))
    #CASO O USUÁRIO DIGITE CARACTERES INVÁLIDOS ENTRARÁ NESSA CONDIÇÃO QUE PEDIRÁ PARA TENTAR NOVAMENTE DIGITANDO APENAS NUMEROS
    else:
        print(function.option_error())