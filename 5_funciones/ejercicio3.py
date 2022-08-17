def es_bisiesto(anio):
    #Devuelve True si el anio es bisiesto, y False si no lo es
    return (anio % 4 == 0) and ((anio % 100 != 0) or (anio % 400 == 0))