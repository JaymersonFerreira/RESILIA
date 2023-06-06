'''Atividade: Criando nosso resilog
➔ O QUE FAZER?
Temos como requisito para nossa aplicação os seguintes pontos:
1. Vamos criar as classes para Categorias e Eventos;
2. As categorias tem apenas título por enquanto;
3. Eventos devem ter título, data e categoria;
4. Ao criar um evento uma lista com as possíveis categorias deve aparecer para ajudar o usuário a
saber quais opções ele tem;
5. Cada evento vai ser inserido em um arquivo de texto que vai ficar com nosso log.'''

class Categoria:
    def __init__(self, titulo):
        self.titulo = titulo


class Evento:
    def __init__(self, titulo, data, categoria):
        self.titulo = titulo
        self.data = data
        self.categoria = categoria


def inicializar_categorias():
    # Função para inicializar as categorias predefinidas
    categorias = [
        Categoria("Aula"),
        Categoria("Show"),
        Categoria("Entrevista"),
        # Adicione mais categorias conforme necessário
    ]
    return categorias


def criar_evento(categorias):
    print("Selecione uma categoria para o evento:")
    for i, categoria in enumerate(categorias):
        print(f"{i + 1}. {categoria.titulo}")

    categoria_escolhida = input("Digite o número da categoria: ")
    categoria_escolhida = int(categoria_escolhida) - 1

    if 0 <= categoria_escolhida < len(categorias):
        titulo = input("Digite o título do evento: ")
        data = input("Digite a data do evento: ")

        evento = Evento(titulo, data, categorias[categoria_escolhida])
        salvar_evento(evento)  # Chamada para a função que salva o evento no arquivo de log
        print("Evento criado com sucesso!")
    else:
        print("Categoria inválida.")


def salvar_evento(evento):
    # Função para salvar o evento no arquivo de log
    with open("log.txt", "a") as arquivo_log:
        arquivo_log.write(f"Título: {evento.titulo}, Data: {evento.data}, Categoria: {evento.categoria.titulo}\n")


if __name__ == "__main__":
    categorias = inicializar_categorias()  # Inicializa as categorias predefinidas
    criar_evento(categorias)  # Permite ao usuário criar um evento e salva-o no arquivo de log