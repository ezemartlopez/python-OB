archivo = open("archivo.txt","w+")
archivo.write("#un comentario\n")
archivo.close()

leer = open("archivo.txt","r")
for linea in leer.readlines():
    print(linea)
leer.close()
print('====================================')
archivo = open('archivo.txt','a')
archivo.write("unaVariable = 123\n")
archivo.close()

leer = open("archivo.txt","r")
for linea in leer.readlines():
    print(linea)
leer.close()