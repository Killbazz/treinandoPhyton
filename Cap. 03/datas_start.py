#
# Arquivo com exemplos de manipulação de  datas
#

from datetime import date
from datetime import time
from datetime import datetime

def ManipulaDataHora():
    hoje = date.today()
    print ("Hoje é:" , hoje)
    print ("Partes da Data: " , hoje.day, hoje.month, hoje.year)
    print ("Numero do dia da Semana: " , hoje.weekday())
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    print("Nome abreviado do dia da semana: " , dias[hoje.weekday()])

    data=datetime.now()
    print ("Data e Hora: " , data)

    tempo = datetime.time(data)
    print ("Hora Atual: " , tempo)

    ManipulaDataHora()

