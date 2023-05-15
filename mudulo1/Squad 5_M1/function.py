from time import sleep

#Neste arquivo está contido todas as funções utilizadas no chatbot.
#Tambem foi importado a biblioteca time, mais precisamente a função SLEEP para ser utilizada em algumas funções.


#ESTA FUNÇÃO É APENAS PARA DAR UMA MELHORADA NO VISUAL DA MENSAGEM DE BOAS VINDAS.
def enfeite():
    return print('-'*80)

#ESTA FUNÇÃO É PARA DAR AS BOAS VINDAS AO USUÁRIO.
def boasVindas(usuario):
    enfeite()
    print('\n')
    print(f'Olá Sr(a) {usuario}, eu sou o Zac, seu assistente virtual da Energy.\n')
    sleep(1)
    print('Por aqui posso te ajudar com diversos serviços.\nPara serviços não listados aqui, consulte pelo nosso\natendimento humano ligando para (99) 9.9999-9999.\n')
    sleep(1)
    print('Caso queira prosseguir digite SIM, ou digite NÃO para finalizar o atendimento.')
    print('\n')
    enfeite()

#ESTA FUNÇÃO DÁ A MENSAGEM FINAL CASO O ATENDIMENTO SEJA ENCERRADO.
def encerra_atendimento(usuario):
    print(f'\nTudo bem Sr(a) {usuario}, voce optou por encerrar o atendimento.\nLembrando que, se precisar entrar em contato,\nestarei por aqui para te atender.\n\nTCHAU TCHAU')

#ESTA FUNÇÃO DIZ AO USUÁRIO QUE A OPÇÃO ESCOLHIDA É INVALIDA.
def option_error():
    print('\nOpção incorreta. Tente novamente digitando apenas numeros!')

#ESTA FUNÇÃO É ACIONADA AO FINAL DE CADA RESPOSTA QUESTIONANDO AO USUÁRIO SE ELE DESEJA ALGO MAIS.
def algo_mais():
    print('Posso ajudar em algo mais?\n')

#ESTA FUNÇÃO É APENAS PARA DAR UM VISUAL AO USUÁRIO DE QUE SUA SOLICITAÇÃO ESTÁ SENDO ENVIADA.
def tempo():
    for cont in range(0, 4):
        print('\nENVIANDO...')
        sleep(0.5)
    
#AQUI ESTÁ O MENU PRINCIPAL.
def menu1(usuario):
    variavel1 = (f'\nTudo bem Sr(a) {usuario}.\nDentre as opções abaixo, no que eu posso ajudar?\n\nDIGITE O NÚMERO DA OPÇÃO DESEJADA!')
    variavel2 = ('1 - 2ª Via de boletos;')
    variavel3 = ('2 - Informar falta de energia;')
    variavel4 = ('3 - Religação;')
    variavel5 = ('4 - Sobre a Energy;')
    variavel6 = ('5 - Encerrar atendimento.')

#AQUI ESTÁ O MENU 1_1.
def menu_1_1():
    print('\nComo deseja receber sua 2ª Via?\n')
    print('1 - E-mail;')
    print('2 - Whatsapp;')
    print('3 - Código via SMS;')
    print('4 - Voltar ao Menu Anterior;')
    print('5 - Encerrar.')

#AQUI ESTÁ O MENU 1_2.
def menu_1_2():
    print('\nSobre a falta de energia:\n')
    print('1 - É em todo o bairro;')
    print('2 - É apenas em sua rua;')
    print('3 - É apenas em sua casa;')
    print('4 - Voltar ao Menu Anterior;')
    print('5 - Encerrar.')

#AQUI ESTÁ O MENU 1_3.
def menu_1_3():
    print('\nSobre a religação:\n')
    print('1 - É para voce (seu CPF);')
    print('2 - Para terceiros;')
    print('3 - Para empresas;')
    print('4 - Voltar ao Menu Anterior;')
    print('5 - Encerrar.')

#AQUI ESTÁ O MENU 1_4.
def menu_1_4():
    print('\nO que deseja saber sobre a Energy?\n')
    print('1 - Sobre Nós;')
    print('2 - Clientes e Fornecedores;')
    print('3 - Sustentabilidade;')
    print('4 - Voltar ao Menu Anterior;')
    print('5 - Encerrar.')

#ESTA FUNÇÃO É APENAS PARA DAR UM VISUAL AO USUÁRIO DE QUE AS INFORMAÇÕES ESTÃO SENDO PROCESSADAS.
def localizar():
    print('\nLOCALIZANDO E ENVIANDO EQUIPE...')
    sleep(0.5)
    print('LOCALIZANDO E ENVIANDO EQUIPE...')
    sleep(0.5)
    print('LOCALIZANDO E ENVIANDO EQUIPE...')
    sleep(0.5)
    print('LOCALIZANDO E ENVIANDO EQUIPE...')
    sleep(0.5)

#ESTA FUNÇÃO É APENAS PARA DAR UM VISUAL AO USUÁRIO DE QUE AS INFORMAÇÕES PESSOAIS ESTÃO SENDO PROCESSADAS.
def localizar_titular():
    print('\nBUSCANDO INFORMAÇÕES...')
    sleep(0.5)
    print('BUSCANDO INFORMAÇÕES...')
    sleep(0.5)
    print('BUSCANDO INFORMAÇÕES...')
    sleep(0.5)
    print('BUSCANDO INFORMAÇÕES...')
    sleep(0.5)

#ÁREA 'SOBRE NÓS' DA ENERGY
def sobre_nos():
    enfeite()
    print('\nSomos uma empresa especializada em transmissão e distribuição de energia.')
    sleep(0.4)
    print('\nNosso diferencial está na habilidade que temos para a concepção e implantação de projetos,')
    print('soluções de tecnologia para levar até a residencia de cada um, energia limpa')
    print('proveniente de fontes renovavéis.\n')
    enfeite()

#MENU EXEMPLO USADO PARA DIGITAR TODOS OS OUTROS.
def menu_exemplo():
    print(':')
    print('1 - ;')
    print('2 - ;')
    print('3 - ;')
    print('4 - Voltar ao Menu Anterior;')
    print('5 - Encerrar.')
