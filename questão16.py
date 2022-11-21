from statistics import mean
"""Faça uma função que leia um número não determinado de valores positivos
e retorna a média aritmética dos mesmos.
- fazer uma função que recebe uma lista com um número indertermina
do de valores decimais pocitivos.
- Essa função retorna a média aritiméticas dos números da lista. Usar
a função mean da biblioteca statistics
"""
def calcula_media(l):
    for value in l:
        if type(value) != int and type(value) != float:
            return Exception
    avg = mean(l)
    return round(avg, 2)

assert calcula_media([2, 3, 5, 1, 6, 4, 3]) == 3.43
assert calcula_media([4, 3.4, 23, 5.4]) == 8.95
assert calcula_media([2, 4, 6, 'nove', True]) == Exception
print('Todos os testes estão OK')
