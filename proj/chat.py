from biblio import *
from time import sleep


boas_vindas()


#// PRINCIPAL
voltar_inicio = False
consulta = ''
duvida = ''

while True:
    if duvida == '4' or consulta == '5' or voltar_inicio == '4':
        break
    sleep(0.5)
    opcoes = ['1_ Dúvidas sobre Steam',
              '2_ Dúvidas sobre PlayStation 4',
              '3_ Dúvidas sobre Xbox One',
              '4_ Sair']

    duvida = intro_duvida(opcoes)
    if duvida == '4' or consulta == '5':
        break
    sleep(0.5)
    if duvida == '1':
        opcoes = ['\n1_ Quais os 10 jogos mais vendidos?',
                  '2_ Quais os 10 jogos mais bem avaliados?',
                  '3_ Quais os 10 mais jogados?',
                  '4_ Retornar ao início',
                  '5_ Sair']

        while True:
            consulta = intro_consulta(opcoes)
            if consulta in ['4', '5']:
                break
            if consulta == '1':
                print('\nEntre os jogos mais vendidos os 10 primeiros são:\n1. Counter Strike\n2. eFootball 2023\n3. EA Sports FIFA 23\n4. Age for Empires IV\n5. PUBG\n6. Subnautica\n7. Euro Truck Simulator 2\n8. Dota 2\n9. RimWorld\n10. Rust')
                print('Mais informações consulte https://pt.wikipedia.org/wiki/Lista_de_jogos_eletr%C3%B4nicos_mais_vendidos')
            elif consulta == '2':
                print('\nNos 10 mais bem avaliados estão:\n1. Hades\n2. Factorio\n3. Phasmophobia\n4. Half-Life: Alyx\n5. Helltaker\n6. The Henry Stickmin Collection\n7. Risk ok Rain 2\n8. Deep Rock Galactic\n9. Persona 4 Golden\n10. Satisfactory\n10. Ultrakill')
                print('Mais informações consulte https://www.techtudo.com.br/listas/2022/12/10-melhores-jogos-de-2022-para-playstation-de-acordo-com-o-metacritic.ghtml')
            elif consulta == '3':
                print('\nOs 10 mais jogados da Steam são:\n1. Dota 2\n2. Goose Goose Duck\n3. Call of Duty: Modern Warfare 2\n4. CS:GO\n5. ARK: Survival Evolved\n6. Destiny 2\n7. PUBG: Battlegrounds\n8. Elden Ring\n9. Apex Legends\n10. Dying Light 2 Stay Human')
                print('Mais informações sobre esse ranking consulte o site https://www.adrenaline.com.br/games/pc-games/confira-os-titulos-mais-jogados-no-steam-em-2022/')
            voltar_inicio = saida_volta()
            if voltar_inicio == '4':
                break
    
    elif duvida == '2':
        sleep(0.5)
        opcoes = ['\n1_ Quais os 10 jogos mais vendidos?',
                  '2_ Quais os 10 jogos mais bem avaliados?',
                  '3_ Quais os 10 mais jogados?',
                  '4_ Retornar ao início']

        while True:
            consulta = intro_consulta(opcoes)
            if consulta in ['4', '5']:
                break
            if consulta == '1':
                print("\nOs 10 jogos mais vendidos do PlayStation 4 são:\n1. Grand Theft Auto V (24 MILHÕES UNIDADES)\n2. Marvel's Spider-Man (20 MILHÕES UNIDADES)\n3. God of War (19,5 MILHÕES UNIDADES)\n4. Uncharted 4: A Thief's End (16 MILHÕES UNIDADES)\n5. The Witcher 3: Wild Hunt (10,8 MILHÕES UNIDADES)\n6. Horizon Zero Dawn (10 MILHÕES UNIDADES)\n7. The Last of Us Remastered (10 MILHÕES UNIDADES)\n8. The Last of Us Part II (10 MILHÕES UNIDADES)\n9. Gran Turismo Sport (8 MILHÕES UNIDADES)\n10. Ghost of Tsushima (8 MILHÕES UNIDADES)")
                print('Mais informações consulte https://pt.wikipedia.org/wiki/Lista_de_jogos_mais_vendidos_para_PlayStation_4')
            elif consulta == '2':
                print('\nNos 10 jogos mais bem avaliados do PlayStation 4 estão:\n1. Elden Ring\n2. God of War - Ragnarok\n3. The Last of Us Parte 1\n4. Horizon: Forbidden West\n5. Return to Monkey Island\n6. Gran Turismo 7\n7. Uncharted: Legacy of Thieves Collection\n8. Cult of the Lamb\n9. Tactics Ogre: Reborn\n10. Tunic')
                print('Mais informações consulte https://www.techtudo.com.br/listas/2022/12/10-melhores-jogos-de-2022-para-playstation-de-acordo-com-o-metacritic.ghtml')
            elif consulta == '3':
                print("\nJá nos 10 mais jogados do PlayStation 4 estão:\n1. Red Dead Redemption 2\n2. Grand Theft Auto V\n3. Persona 5 Royal\n4. The Last of US Remastered\n5. God of War\n6. Metal Gear Solid V: The Phantom Pain\n7. Uncharted 4: A Thief's End\n8. Bloodborne\n9. The Witcher III: Wild Hunt\n10. Final Fantasy XIV: Shadowbringers")
                print('Mais iformações consulte https://www.adrenaline.com.br/games/playstation/top-10-veja-lista-de-jogos-de-ps4-e-ps5-mais-baixados-em-junho-na-ps-store-brasil/')
            voltar_inicio = saida_volta()
            if voltar_inicio == '4':
                break

    elif duvida == '3':
        sleep(0.5)
        opcoes = ['\n1_ Quais os 10 jogos mais vendidos?',
                  '2_ Quais os 10 jogos mais bem avaliados?',
                  '3_ Quais os 10 mais jogados?',
                  '4_ Retornar ao início?']
        while True:
            consulta = intro_consulta(opcoes)
            if consulta in ['4', '5']:
                break
            if consulta == '1':
                print("\nOs 10 jogos mais vendidos do Xbox One são:\n1. Halo 5: Guardians (5 MILHÕES UNIDADES)\n2. Call of Duty: Infinite Warfare (3.9 MILHÕES UNIDADES)\n3. FIFA 17 (3.6 MILHÕES UNIDADES)\n4. Cuphead (3 MILHÕES UNIDADES)\n5. Gears of War 4 (2.6 MILHÕES UNIDADES)\n6. Dead Rising 3 (2.6 MILHÕES UNIDADES)\n7. Forza Horizon 3 (2.5 MILHÕES UNIDADES)\n8. Tom Clancy's The Division (2.4 MILHÕES UNIDADES)\n9. Madden NFL 17 (2 MILHÕES UNIDADES)\n10. Forza Motorsport 5 (2 MILHÕES UNIDADES)")
                print('Mais informações consulte https://pt.wikipedia.org/wiki/Lista_de_jogos_mais_vendidos_para_Xbox_One')
            elif consulta == '2':
                print("\nJá entre os 10 com melhores avaliações estão:\n1. Elden Ring\n2. Forza Horizon 5\n3. Gears 5\n4. Halo Infinite\n5. Microsoft Flight Simulator\n6. Ori and the Will of the Wisps\n7. Outer Wilds\n8. Psychonauts 2\n9. Sea of Thieves\n10. Tunic")
                print('Mais informações consulte https://canaltech.com.br/games/os-melhores-jogos-do-xbox-one/')
            elif consulta == '3':
                print('\nE entre os 10 mais jogados estão:\n1. Red Dead Redemption 2\n2. Hellblade: Senua’s Sacrifice\n3. Grand Theft Auto V\n4. Hades\n5. Resident Evil 2\n6. The Witcher 3: Wild Hunt\n7. Ori and the Will of the Wisps\n8. Cuphead\n9. Fortnite\n10. Forza Horizon 5')
                print('Mais informações sobre esse ranking consulte https://www.adrenaline.com.br/games/xbox/lista-revela-jogos-mais-populares-do-xbox-em-2022-minecraft-lidera/')

            voltar_inicio = saida_volta()
            if voltar_inicio == '4':
                break

print('Agradecemos a visita.')