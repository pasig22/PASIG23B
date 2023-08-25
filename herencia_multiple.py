#Herencia multiple
class MiSuperClase1():
 
    def metodo_1(self):
        print("Metodo llamado de MisuperClase1")
 
class MiSuperClase2():
 
    def metodo_2(self):
        print("Metodo llamado de MisuperClase2")

# Clase que hereda las 2 clases anteriormente definidas
class MiClase(MiSuperClase1, MiSuperClase2):
 
    def metodo_3(self):
        print("Metodo llamado de MisuperClase3")

# Se crea el objeto "c" y luego se llama al metodo_1 y metodo_2 heredados de las 2 primeras clases
cl = MiClase()
cl.metodo_1()
cl.metodo_2()	