def fazer_pesquisa():
    respostas = []  # Lista vazia para armazenar as respostas
    while True:
        idade = input("Digite a sua idade (ou 00 para sair): ")  # Pede a idade do participante
        if idade == "00":  # Se o usuário digitar '00', interrompe o laço
            break
        genero = input("Digite o seu gênero (M/F/O): ")  # Pede o gênero do participante
        print("Responda as seguintes perguntas com 1 (Sim), 2 (Não) ou 3 (Não sei responder):")
        respostas_participante = []  # Lista vazia para armazenar as respostas do participante
        for pergunta in PERGUNTAS:  # Para cada pergunta da pesquisa:
            resposta = input(pergunta + " ")  # Pede a resposta do participante
            respostas_participante.append(resposta)  # Adiciona a resposta à lista de respostas do participante
        respostas.append(adicionar_resposta(respostas_participante, idade, genero))  # Adiciona a resposta, idade, gênero e data/hora à lista de respostas
    escrever_csv(respostas)  # Escreve as respostas no arquivo CSV
    print("Pesquisa finalizada. Os resultados foram gravados no arquivo respostas.csv.")  # Informa ao usuário que a pesquisa foi finalizada e os resultados foram gravados no arquivo CSV