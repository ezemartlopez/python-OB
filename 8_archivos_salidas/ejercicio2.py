import pickle

class Vehiculo:
    marca = None
    ruedas = None
    def __init__(self,marca,ruedas):
        self.marca = marca
        self.ruedas = ruedas
    def caracteristicas(self):
        return f"Marca: {self.marca}, ruedas: {self.ruedas}"

#serializando un objeto
arch_bin = open("vehiculo.bin","wb")

mycar = Vehiculo("Audi",4)
pickle.dump(mycar,arch_bin)

arch_bin.close()

#deserializando un objeto
archivo = open("vehiculo.bin","rb")

autito = pickle.load(archivo)
print(autito.caracteristicas())

archivo.close()