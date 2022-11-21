from random import randint
'''Faça uma função que lê 50 valores inteiros e retorna o maior e 
o menor deles.'''

def maior_menor(l):
    for n in l:
        if type(n) != int and type(n) != float:
            return Exception
        elif n < 0:
            return Exception
    return (min(l), max(l))

lista1 = [6, 4, 2, 5, 1, 45, 66, 4, 4, 3, 2, 77, 8, 5, 346, 345, 545, 5, 2, 8, 9, 75, 23, 567, 76,12, 24, 23, 52, 234, 34,212 ,12, 554, 34, 2, 67, 56, 89, 5, 43, 34 ,23, 23, 23, 53, 8, 9, 7, 5]
lista2 = [4, 6, 23, 534, 634, 12, 34, 6, 75, 34, 63, 34, 6,7,8,4,0, 87, 34, 2334, 122,3, 52, 12, 5,34, 345, 77, 8, 5, 4, 23, 24, 63, 23, 67, 45,23, 21, 43, 23, 34,3, 6 ,8 ,77, 86, 56, 65, 56]
lista3 = [2, 34, 76, 5, 45 ,64, 23, 23, 6, 8,7, 5, 4, 45, 5, 34 ,6 ,34 ,34,4, 5, 6,6,3,4, 7,678,45,34,634, 23, 34, 64, 23, 235, 23, 34, 78, 90,56, 45,5, 45, 654, 456, 77, 4 ,455, 34,23]

assert maior_menor(lista1) == (1, 567)
assert maior_menor([2, -54, 4, 34]) == Exception
assert maior_menor(lista2) == (0, 2334)
assert maior_menor(['um', 'dois', 3, 64]) == Exception
print('Todos os testes estão OK.')



