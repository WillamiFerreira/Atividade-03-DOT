'''Faça uma função que recebe, por parâmetro, a altura e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura
- 44.7.'''
def validador_de_tipo(a=0, s=''):
    if a == 0 or s == '': return False
    if type(a) == float or type(a) == int and type(s) == str:
        return True
    else:
        return False
    
def peso_ideal(a=0, s=''):
    if validador_de_tipo(a, s):
        if s in 'Mm': return round(72.7 * a - 58, 2) 
        elif s in 'Ff': return round(62.1 * a - 44.7, 2)
    return Exception

assert peso_ideal(1.78, 'M') == 71.41
assert peso_ideal(1.55, 'F') == 51.56
assert peso_ideal(2.10, 'M') == 94.67
assert peso_ideal(1.78, 't') == Exception
assert peso_ideal(2, 'M') == 87.4
assert peso_ideal('2.12', 2) == Exception
assert peso_ideal(1.44) == Exception
assert peso_ideal('F') == Exception
assert peso_ideal('g') == Exception
print('Todos os testes estão OK \U0001F44D')