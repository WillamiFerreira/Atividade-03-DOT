'''Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente.'''

def ordena_numeros(n1, n2):
    ordenados = list()
    if type(n1) == int and type(n2) == int:
        if n1 < n2:
            ordenados.append(n1)
            ordenados.append(n2)
            return ordenados
        else:
            ordenados.append(n2)
            ordenados.append(n1)
            return ordenados
    else:
        return Exception

assert ordena_numeros(6, 2) == [2, 6]
assert ordena_numeros(3.2, 46) == Exception
assert ordena_numeros(66, -31) == [-31, 66]

print('Todos os testes estão OK \U0001F44D')