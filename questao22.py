from math import factorial
'''Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!'''
def validador_de_entrada(n):
    if type(n) == int and n > 0: return True
    else: return False

def calcula_valor_s(n=None):
    resultado = 0
    if validador_de_entrada(n):
        for v in range(0, n+1):
            fac = factorial(v)
            resultado += 1/fac
        return round(resultado, 2)
    else:
        return Exception

assert calcula_valor_s(5) == 2.72
assert calcula_valor_s('t') == Exception
assert calcula_valor_s(4.33) == Exception
assert calcula_valor_s(-34) == Exception
assert calcula_valor_s() == Exceptionassert calcula_valor_s(-34) == Exception
print('todos dos testes estão OK')

