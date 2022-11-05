"""Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano."""

def valor(n):
    if isinstance(n, float):
        return Exception
    if n <= 0:
        return False
    else:
        return True

assert valor(-6) == False
assert valor(10) == True
assert valor(33.45) == Exception
assert valor(-421) == False
assert valor(0) == False
print('Todos os testes estão OK \U0001F44D')