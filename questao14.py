'''Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se
esses valores podem ser os comprimentos dos lados de um triângulo e, neste
caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um
triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento
de cada lado de um triângulo é menor do que a soma do comprimento dos outros
dois lados. O procedimento deve identificar o tipo de triângulo formado
observando as seguintes definições:

o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.'''

'''
1 - Criar a função que recebe os tres lados como parâmetro. Essa função verifica se
com os valores é possível fazer um triângulo ou não. Se for possível, a função deve
classificar o triângulo.
'''

def triangulo(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        return Exception
    else:
        if (a == b) and (a == c):
            return 'Equilátero'
        elif (a==b) or (a==c) or (b==c):
            return 'Isósceles'
        else:
            return 'Escaleno'


assert triangulo(4, 4, 4) == 'Equilátero'
assert triangulo(10, 56, 9) == Exception
assert triangulo(2, 4, 5) == 'Escaleno'

print('Todos os testes estão OK')