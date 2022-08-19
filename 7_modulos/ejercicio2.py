from datetime import datetime
from datetime import time

def es_hora_de_irse():
    ahora = datetime.now()
    if ahora.hour >= 19:
        print("Es hora de irse a casa.....")
    else:
        falta = ahora.time()
        print("Quedan {}:{}:{} de trabajo.....".format(19-falta.hour,59-falta.minute,59-falta.second))

es_hora_de_irse()
