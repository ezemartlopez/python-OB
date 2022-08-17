def es_primo(numero):
    #Devuelve True si es primo, y False si no lo es
    contador = 0

    for num in range(1,numero+1):
        if (numero % num) == 0:
            contador += 1
    
    return contador <= 1