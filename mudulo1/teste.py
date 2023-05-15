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

#// PRINCIPAL
voltar_inicio = False
consulta = ''
duvida = ''

while True:
    if duvida == '4' or consulta == '5':
        break

    opcoes = ['1_ Dúvidas sobre Codewars',
              '2_ Dúvidas sobre Discord',
              '3_ Dúvidas sobre as aulas',
              '4_ Sair']

    duvida = intro_duvida(opcoes)
    if duvida == '4' or consulta == '5':
        break

    if duvida == '1':
        opcoes = ['1_ link de acesso?',
                  '2_ Classificação?',
                  '3_ Quais tecnologias treinar?',
                  '4_ Retornar ao início',
                  '5_ Sair']

        while True:
            consulta = intro_consulta(opcoes)
            if consulta in ['4', '5']:
                break
            if consulta == '1':
                print('Link de acesso do Qualified é: https://codewars.com')
            elif consulta == '2':
                print('As classificações são usadas para indicar a proficiência dos usuários e a dificuldade do Kata. Existem duas classes de ranks, Kyu e Dan, que são divididas em 8 níveis cada.')
            elif consulta == '3':
                print('Linguagem de programação que podem ser praticadas no Codewars são: C, C#, C++, Dart, Go, Haskell, Java, JavaScript, Kotlin, Lua, PHP, Python, R, Ruby, Rust, SQL, Scala, Solidity, Swift e TypeScript')

            voltar_inicio = saida_volta()
            if voltar_inicio:
                break

    elif duvida == '2':
        opcoes = ['1_ O que é o Discord?',
                  '2_ Por que utilizaremos o Discord?',
                  '3_ Link de acesso?',
                  '4_ Retornar ao início']

        while True:
            consulta = intro_consulta(opcoes)
            if consulta in ['4', '5']:
                break
            if consulta == '1':
                print('O Discord é um aplicativo que ajuda na interação da comunidade, todos nós podemos conversar por lá, enviar comunicados e solicitar suporte.')
            elif consulta == '2':
                print('Porque seŕa pelo nosso servidor no Discord que a Turma poderá interagir com bate-papo, dúvidas, dicas e ajuda. \nTambém por meio da plataforma que a turma receberá os comunicados oficiais.')
            elif consulta == '3':
                print('Link do nosso servido no Discord: https://discord.gg/eX8YrvT3')

            voltar_inicio = saida_volta()
            if voltar_inicio:
                break

    elif duvida == '3':
        opcoes = ['1_ Acesso ás aulas?',
                  '2_ Link do Portal do aluno?',
                  '3_ Dias e horarios?',
                  '4_ Retornar ao início?']
        while True:
            consulta = intro_consulta(opcoes)
            if consulta in ['4', '5']:
                break
            if consulta == '1':
                print('O acesso é a partir do portal do aluno! Lembre-se de entrar no Portal 10 minutinhos antes do início da aula para garantir que tudo esteja certo.')
            elif consulta == '2':
                print('Link do Portal do aluno: https://aluno.resilia.work/')
            elif consulta == '3':
                print('Os dias das aulas são de segunda a quinta-sexta das 15h as 18h')

            voltar_inicio = saida_volta()
            if voltar_inicio:
                break

print('Fim do programa!')