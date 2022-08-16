print("Se mostrara los numeros impares desde un numero de inicio y un final.")
inicio = int(input("Ingrese el inicio: "))
final = int(input("Ingrese el final: "))

lista = []

for num in range(inicio,final+1):
    if (num % 2) != 0:
        lista.append(num)

print(lista)