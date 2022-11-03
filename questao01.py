"""Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
seu volume (v = 4/3 * PI * R**3)."""

def volume(raio):
    if type(raio) == str or raio < 0:
        return Exception
    else:
        return round(4/3 * 3.14 * raio**3, 2)

assert volume(0) == 0
assert volume(-1) == Exception
assert volume("abc") == Exception
assert volume(1.0) == 4.19
assert volume(10) == 4186.67
print('Todos os testes estão OK\U0001F44D')


