"""Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e False em caso
contrário."""
def NumPrimo(n):
    if type(n) != int or n <= 0:
        return Exception
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return False
            else:
                return True

assert NumPrimo(2) == True
assert NumPrimo(8) == False
assert NumPrimo(-45) == Exception
assert NumPrimo(3.4) == Exception
assert NumPrimo(0) == Exception

print('Todos dos testes estão OK. \U0001F44D')
