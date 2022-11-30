from math import factorial

def calcula_fatorial(n=None):
    if type(n) == int: return factorial(n)
    else: return Exception
    
assert calcula_fatorial(3) == 6
assert calcula_fatorial('string') == Exception
assert calcula_fatorial(4.4) == Exception
assert calcula_fatorial(True) == Exception
assert calcula_fatorial() == Exception
print('Todos os testes estão OK')

