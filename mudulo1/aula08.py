# fruta = 'Laranja'
# anterior = 6
# atual = 4

# if anterior == atual:
#     print(f'A {fruta} Manteve o mesmo valor! R$ {anterior:.2f}')
# elif anterior > atual:
#     result = anterior - atual
#     print(f'A {fruta} Abaixou o valor em R$ {result:.2f}', )
# else:
#     result = atual - anterior
#     print(f'A {fruta} Subiu de preço em: R$ {result:.2f}')


# from time import sleep

# num = int(input('Digite um numero para decrementar: '))

# while num >= 0:
#     sleep(0.3)
#     print(num)
#     num = num - 1
# print('Fim')


# inicio = 0
# while inicio % 3 != 0:
#     inicio = int(input('Escreva o número inicial: '))
#     for cont in range(inicio, 0, -3):
#         print(cont)





# paciente = list ()
# ficha = []
# qtd_paciente = int(input('Quantidade de paciente: '))
# for i in range(0, qtd_paciente):
#     nome = str(input('Nome: '))
#     paciente.append(nome)

#     peso = float(input('Peso: '))
#     paciente.append(peso)

#     altura = float(input('Altura: '))
#     paciente.append(altura)

#     imc = peso / (altura * altura) 
#     paciente.append(imc)

#     ficha.append(paciente[:])
#     paciente.clear()
    
# print(ficha)

# salario = float(input('Salario: '))
# if salario < 600:
#     print(f'O salario de {salario} está isento de imposto!')
# elif salario >= 600 and salario <= 1200:
#     calc = (salario * 20) / 100
#     print(f'O salario de {salario} vai pagar {calc} de imposto!')
# elif salario > 1200 and  salario < 2000:
#     calc = (salario * 25) / 100
#     print(f'O salario de {salario} vai pagar {calc} de imposto!')
# elif salario > 2000:
#     calc = (salario * 35) / 100
#     print(f'O salario de {salario} vai pagar {calc} de imposto!')


# def funcao(a, b, c):
#     maior = a
#     if b > maior:
#         maior = b
#     if c > maior:
#         maior = c
    
#     return print(f'O maior é o {maior}')
         

# n1 = 2
# n2 = 5
# n3 = 7

# funcao(n1, n2, n3)


# num  = int(input('Digite um número: '))
# fatorial = 1
# for cont in range(num, 1, -1):
#     fatorial *= cont
# print(f'O fatorial de {num} é {fatorial}')

def conferir(letra):
    if letra in 'aeiou':
        print(f'A letra {letra} é uma vogal!')
    else:
        print(f'A letra {letra} é uma consoante!')
    


letra = str(input('Digite uma letra: ')).lower().strip()[0]

conferir(letra)

