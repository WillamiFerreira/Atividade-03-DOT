'''Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o número de divisores desse valor.'''

def divisores(n):
    divs = 0
    if type(n) != int or n < 0:
        return Exception

    for i in range(1, n+1):
        if n % i == 0:
            divs += 1
    return divs

assert divisores(225) == 9
assert divisores('dez') == Exception
assert divisores(-76) == Exception
assert divisores(135) == 8
print('Todos os testes estão OK')