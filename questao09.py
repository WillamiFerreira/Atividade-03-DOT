"""Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
ímpar. A função deve retornar um valor booleano."""


def imparPar(valor):
    if valor <= 0 or isinstance(valor, float):
        return Exception
    if valor % 2 == 0:
        return True
    else:
        return False

assert imparPar(5) == False
assert imparPar(4) == True
assert imparPar(5.44) == Exception


print('Todos os testes estão OK \U0001F44D')