'''Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve
a tabuada de 1 até N. Mostre a tabuada na forma:
1 x N = N
2 x N = 2N
...
N x N = N2'''

def tabuada(n):
    resultados = list()
    for i in range(1, n+1):
        n = 4 * i
        resultados.append(n)
    for ind,r in enumerate(resultados):
        print(f'{ind+1}x4 = {r}')

#tabuada(4)
assert tabuada(4) == ()