"""Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:"""

def nota(i):
    if i < 0:
        print('Não é possível atribuir uma nota negativa.')
    elif 0 <= i <=4.9:
        return 'D'
    elif 5<=i<=6.9:
        return "C"
    elif 7 <= i <= 8.9:
        return "B"
    elif 9 <=i<= 10:
        return "A"
    else:
        return "Uma nota não pode ser maior que 10"

assert nota(6) == "D"
assert nota(9) == "A"
print('Todos os testes OK')    
