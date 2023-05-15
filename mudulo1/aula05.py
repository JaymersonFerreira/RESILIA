# idade1 = 24
# idade2 = 20

# idade3 = idade1

# print('idade1:', idade1)
# print('idade2:', idade2)

# idade1 = idade2
# print('idade1:', idade1)

# idade2 = idade3
# print('idade2:', idade2)


# salario = 1000
# reajuste = 3.3
# novoSalario = salario + (salario * reajuste / 100)
# print(novoSalario)

# while True:
#     msg = str(input('Digite algo: '))
#     print('Você digitou: ',msg)
#     resp = input('Quer continuar? ').upper()[0]
#     if resp == 'N':
#         break
# print('Fim!!')


def funcao1(a, b, c, d):
    return print('Prinmeira Função: ', a*c - b*d)

def funcao2(a, b, c, d):
    return print('Segunda Função: ',(a + b + c + d)/4)

a = 1
b = 2
c = 3
d = 4

funcao1(a, b, c, d)
funcao2(a, b, c, d)
