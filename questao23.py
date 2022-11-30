'''Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3)'''

def encontra_valor_s(n=None):
    if type(n) == int and n > 0:
        resultado = 0
        for v in range(1, n+1):
            resultado += (n*2 + 1)/(n+3)
        return round(resultado, 2)
    else:
        return Exception

assert encontra_valor_s(10) == 16.15
assert encontra_valor_s(-34) == Exception
assert encontra_valor_s('string') == Exception
assert encontra_valor_s(4.221) == Exception
assert encontra_valor_s() == Exception
print('Todos os testes estão OK')