"""Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma
letra. Se a letra for A o procedimento calcula a média aritmética das notas do
aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
a média calculada."""

def Calcula_Media(n1, n2, n3, letra):
    if letra in "Aa" :
        media = round(((n1 + n2 + n3) / 3), 2)
        return media
    elif letra in "Pp":
        media = round(((n1 * 5) + (n2 *3) + (n3*2)) / 10, 2)
        return media
    else:
        return Exception

try:
    assert Calcula_Media(8.5, 9, 10, "A" ) == 9.17
    assert Calcula_Media(6.7, 10, 2, "P") == 6.75
    assert Calcula_Media(5, 6.7, 8.9, "z") == Exception
   #assert Calcula_Media(4, 5, "A") == Exception
except TypeError:
    print('Faltando notas ou tipo de operação.')
else:
    print('Todos os testes estão OK. \U0001F44D')
