"""Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano."""

def valor(n):
    if n < 0:
        return False
    else:
        True

assert valor(-6) == False
assert valor(10) == True
print('Todos os testes estão OK')