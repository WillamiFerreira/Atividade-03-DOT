'''Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula
e retorna Xz. (sem utilizar funções ou operadores de potência prontos)'''
def verificador(x, y):
    if x == None or y == None: return False
    if type(x) == int or type(x) == float:
        if type(y) != int:
            return False
        else: return True
    else: return False

def potenciacao(x=None, y=None):
    if verificador(x, y):
        resultado = 1
        for _ in range(y):
            resultado *= x
        return round(resultado, 2)
    else:
        return Exception

assert potenciacao(2, 2) == 4
assert potenciacao(10, 2) == 100
assert potenciacao(21.4, 2) == 457.96
assert potenciacao(2, 2.3) == Exception
assert potenciacao() == Exception
assert potenciacao('string', 'string') == Exception
print('Todos os testes estão OK')
