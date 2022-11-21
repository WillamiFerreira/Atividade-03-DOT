'''Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.

S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.'''

def encontra_valor_s(n):
    resultado = 0
    if type(n) != int or n < 0:
        return Exception
    for i in range(2, n+1):
        resultado += 1/i
    return round(resultado + 1, 2)

assert encontra_valor_s(12) == 3.1
assert encontra_valor_s(5) == 2.28
assert encontra_valor_s('string') == Exception
assert encontra_valor_s(-45) == Exception
print('Todos os testes estão OK')