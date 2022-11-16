import datetime
'''Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
O procedimento deve retornar, também por parâmetro, a duração do jogo em
horas e minutos, considerando que o tempo máximo de duração de um jogo é
de 24 horas e que o jogo pode começar em um dia e terminar no outro.'''

def diferenca_tempo(ti, tf):
    data_inicial = datetime.datetime(ti)
    data_final = datetime.datetime(tf)
    duracao_jogo = data_final - data_inicial
    return str(duracao_jogo)


assert diferenca_tempo((2022, 4, 27, 13), (2022, 4, 27, 16, 6)) == '3:06:00'


#... Não consegui responder essa 🥲