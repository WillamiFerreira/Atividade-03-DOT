"""Faça uma função que recebe, por parâmetro, a altura e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura
- 44.7."""

def peso_ideal(a, s):
    if s == "F":
        peso_ideal = round(72.7 * a - 58, 2)
        print(peso_ideal)
    elif s == "M":
        peso_ideal = round(72.7 * a - 58, 2)
    else:
        print('Escolha invalida')

assert peso_ideal(1.79, "M") == 72.13
assert peso_ideal(1.55, "F")