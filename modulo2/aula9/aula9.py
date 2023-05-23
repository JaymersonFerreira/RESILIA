# inglesPort = {'one': 'um', 'two': 'dois', 'three': 'três'}
# inglesPort[0] = 'zero'

# #acessando valores ds chaves
# print(inglesPort['two'])
# print(inglesPort.get('Two'))
# print(inglesPort.keys())


# #acessar os valores pelos alementos
# print(inglesPort.values())

# #retorna os itens de um dicionarios na formato de tuplas
# print(inglesPort.items())

# inglesPort = {'one': 'um', 'two': 'dois', 'three': 'três', 'four': 'quatro'}
#  #usando atribuição
# inglesPort['one'] = 'uno'
# #usando o metodo update
# inglesPort.update({'two': 'dos'})

# # print(inglesPort)

# #remove pela chave
# # inglesPort.pop('one')

# # del inglesPort['two']

# # inglesPort.popitem()

# #esvasiar pelo ultimo item inserido
# inglesPort.clear()

# print(inglesPort)

# inglesPort = {'one': 'um', 'two': 'dois', 'three': 'três', 'four': 'quatro'}
# print(inglesPort)

# inglesPort['one'] = 1
# inglesPort['two'] = 2
# inglesPort['three'] = 3
# inglesPort['four'] = 4
# print(inglesPort)

# # inglesPort.popitem()
# inglesPort.pop('two')
# inglesPort.pop('three')
# inglesPort.pop('four')
# print(inglesPort)

# inglesPort.clear()
# print(inglesPort)



# inglesPort = {'one': 'um', 'two': 'dois', 'three': 'três'}

# #iterar os elementos de um dicionário

# for chave in inglesPort:
#     print(f"O item '{chave}' possui o valor '{inglesPort[chave]}' no dicionário")

# for chave, valor in inglesPort.items():
#     print(f"Os valores da tupla são chave  '{chave}'  e valor  '{valor}'")


inglesPort = {'one': 'um', 'two': 'dois', 'three': 'três'}

#__faz copia__
dict_copia = dict(inglesPort)

dict_copia['one'] = 'uno'

print(dict_copia)

print(inglesPort)

# Dicionário com as pessoas que responderam (True) ou não responderam (False) à enquete
respostas = {
    "Aline": True,
    "Daniel": False,
    "Jeff": True
}


# Lista de pessoas que devem participar da enquete
pessoas = ["Aline", "Daniel", "Edineudo", "Rodrigo", "Jeff"]

# Verifica se as pessoas que devem participar da enquete estão presentes no dicionário de respostas
for pessoa in pessoas:
    if pessoa in respostas:
        if respostas[pessoa]:
            print(f"Obrigado, {pessoa}, por responder à enquete sobre sua linguagem favorita!")
        else:
            print(f"{pessoa}, você ainda não respondeu à enquete. Por favor, participe!")
    else:
        print(f"{pessoa}, você ainda não respondeu à enquete. Por favor, participe!")