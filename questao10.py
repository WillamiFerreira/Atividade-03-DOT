"""Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:"""

def nota(i):
    if i < 0:
        return Exception
    elif 0 <= i <=4.9:
        return 'D'
    elif 5<=i<=6.9:
        return "C"
    elif 7 <= i <= 8.9:
        return "B"
    elif 9 <=i<= 10:
        return "A"
    else:
        return Exception

assert nota(6) == "C"
assert nota(9) == "A"
assert nota(7.6) == "B"
assert nota(-5) == Exception
assert nota(12) == Exception
print('Todos os testes OK \U0001F44D')    
