"""Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo:"""

def idade(i):
    if i < 5:
        return Exception
    elif 5 <= i <=7:
        return 'Infantil A'
    elif 8<=i<=10:
        return "Infantil B"
    elif 11 <= i <= 13:
        return "Juvenil A"
    elif 14 <=i<= 17:
        return "Juvenil B"
    else:
        return "Adulto"

assert idade(6) == "Infantil A"
assert idade(55) == "Adulto"
assert idade(2) == Exception
assert idade(13) == "Juvenil A"

print('Todos os testes OK \U0001F44D')    
