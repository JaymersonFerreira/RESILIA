#criar uma nova função que será utilizada dentro do retorno da função calculaDobroDaSoma
#e essa função deve imprimir o resultado da seguinte forma:
#'A soma do valor1 mais o valor2 é igual ao resultado e seu dobro é igual ao dobro'

def soma(valor1, valor2):
    result = valor1 + valor2
    return result


def mult(valor1, valor2):
    result = soma(valor1, valor2)
    dobro  = result * 2
    return print_dobro(valor1, valor2, result, dobro)


def print_dobro(valor1, valor2, result, dobro):
    soma(valor1, valor2)
    print(f'A soma do {valor1} mais o {valor2} é igual ao {result} e seu dobro é igual ao {dobro}')


print_dobro(2, 2, a=0, b=0)