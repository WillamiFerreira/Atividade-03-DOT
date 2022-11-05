"""Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano."""
def valor(numero):
    soma = 0
    if numero <= 0:
        return Exception
    for n in range(1, numero):
        if numero % n == 0: 
            soma += n
    if soma == numero:
        return True
    else:
        return False 

assert valor(6) == True
assert valor(28) == True
assert valor(423) == False
assert valor(-3) == Exception

print('Todos os testes estão OK \U0001F44D')