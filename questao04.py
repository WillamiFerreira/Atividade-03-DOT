"""Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos."""

def Conversor(segundos):
    if segundos > 0:
        segundos = segundos % (24 * 3600) 
        horas = segundos // 3600
        segundos %= 3600
        minutos = segundos // 60
        segundos %= 60
    else:
        return Exception
      
    return "%d:%02d:%02d" % (horas, minutos, segundos) 

assert Conversor(12345) == "3:25:45"
assert Conversor(3600) == "1:00:00"
assert Conversor(-8686) == Exception
print('Todos os testes estão OK. \U0001F44D')