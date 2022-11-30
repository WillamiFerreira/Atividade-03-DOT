"""Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o somatório desse valor."""
def somador(n):
    somatorio = 0
    if type(n) != int or n < 0: return Exception
    for i in range(1, n+1):
        somatorio += i
    return somatorio


assert somador(10) == 55
assert somador(15) == 120
assert somador(-66) == Exception
assert somador('string') == Exception
print('Todos os testes estão OK')