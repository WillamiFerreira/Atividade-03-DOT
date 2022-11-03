"""Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
ímpar. A função deve retornar um valor booleano."""

def valor(n):
    if n % 2 == 0:
        return True
    else:
        return False


assert valor(5) == False
assert valor(6) == True
print('Tudo certo')