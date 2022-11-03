"""Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano."""
def valor(numero):
    soma = 0
    for n in range(1, numero, -1):
        if type(numero/n) == int:
            soma += n
        else:
            pass
    print(soma)
    if soma == numero:
        return True
    else:
        return False 

assert valor(6) == True
print('Tudo certo')