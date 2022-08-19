"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos 
impares de una lista pasada por parámetro con filter y realizará una suma de todos 
estos elementos obtenidos mediante reduce.
"""
from functools import reduce
def impar(number):
    return number %2 != 0

def suma(a,b):
    return a+b

elementos = [1,2,3,4,5,6,7,8,9,11,3,4,20,56,57,90,100,17]

impares = list(filter(impar,elementos))

print(f'Elememtos impares: {impares}')

suma = reduce(suma,impares)

print(f'La suma de los impares es: {suma}')