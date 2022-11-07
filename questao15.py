'''A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
coletando dados sobre o salário e número de filhos. Faça uma função que leia
esses dados para um número não determinado de pessoas e retorne a média de
salário da população, a média do número de filhos, o maior salário e o percentual
de pessoas com salário até R$ 350,00.'''

'''
1 - Fazer uma função que leia salário e número de filhos de um número inderteminado
de pessoas (usar dicionários).
2 - retonar a média de salário, média de filhos e o maior salário e o percentual de
pessoas com salário 350,00 reais.
'''
def funcao(dados):
    new_data = list()
    media_salario = 0
    media_filhos = 0
    maior_salario = 0
    perc_sal_350 = 0

    for i in dados.values():
        media_salario += i[0]
        media_filhos += i[1]
        if i[0] > maior_salario:
            maior_salario = i[0]
        if i[0] < 350:
            perc_sal_350 += 1

    perc_sal_350 /= 100    
    media_salario /= len(dados)
    media_filhos/=len(dados)

    new_data = [media_salario, media_filhos, maior_salario, perc_sal_350]
    return new_data


dados = {1 : [5000, 2], 2 : [1200, 4]}
assert funcao(dados) == [3100.0, 3, 5000, 0 ]
print('Todos os testes estão OK \U0001F44D')