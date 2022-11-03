"""Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias."""

def idade(a, m, d):
    dias = 0
    dias += a *365
    dias += m * 30
    dias += d
    return dias

assert idade(56, 9, 20) == 20730
assert idade(10, 2, 24) == 3734

print("Todos os testes estão OK. \U0001F44D")