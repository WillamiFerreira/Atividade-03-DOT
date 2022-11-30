'''Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente.'''

def ordena_numeros(n1=None, n2=None):
    ordenados = [n1, n2]
    if n1 == None or n2 == None: return Exception
    if type(n1) == int and type(n2) == int:
        ordenados.sort()
        return ordenados
    else:
        return Exception

assert ordena_numeros() == Exception
assert ordena_numeros(4) == Exception
assert ordena_numeros(6, 2) == [2, 6]
assert ordena_numeros(3.2, 46) == Exception
assert ordena_numeros(66, -31) == [-31, 66]
assert ordena_numeros('3', '55') == Exception

print('Todos os testes estão OK \U0001F44D')