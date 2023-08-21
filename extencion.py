class Extension:
    def __init__(self, nombre, x1, y1, x2, y2):
        self.nombre = nombre
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_x1(self):
        return self.x1

    def set_x1(self, x1):
        self.x1 = x1

    def get_y1(self):
        return self.y1

    def set_y1(self, y1):
        self.y1 = y1

    def get_x2(self):
        return self.x2

    def set_x2(self, x2):
        self.x2 = x2

    def get_y2(self):
        return self.y2

    def set_y2(self, y2):
        self.y2 = y2

    def ancho(self):
        return abs(self.x2 - self.x1)

    def alto(self):
        return abs(self.y2 - self.y1)

    def area(self):
        return self.ancho() * self.alto()

    def circunferencia(self):
        return 2 * self.ancho() + 2 * self.alto()

# Solicitar datos al usuario
nombre_municipio = input("Ingrese el nombre del municipio: ")
x1 = float(input("Ingrese la coordenada x1: "))
y1 = float(input("Ingrese la coordenada y1: "))
x2 = float(input("Ingrese la coordenada x2: "))
y2 = float(input("Ingrese la coordenada y2: "))

# Crear una instancia de la clase Extension
extension_municipio = Extension(nombre_municipio, x1, y1, x2, y2)

# Obtener información de la extensión
print("Nombre del municipio:", extension_municipio.get_nombre())
print("Área:", extension_municipio.area())
print("Circunferencia:", extension_municipio.circunferencia())
