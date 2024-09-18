print("--Programacion POO--")
# definicion de clases
class Perro:
    # funciones dentro de la cla
    def morder(self):
        print("El perro me ladro")
    def Datos_perro(self,nombre,edad):
            print(f" Nombre : {nombre} edad : {edad}")


# zona creacion de objetos
pitbull=Perro()

# zona de uso de objetos

pitbull.Datos_perro("Rocky",4)
pitbull.morder()