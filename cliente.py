


class Cliente:
    def __init__(self, id, nombre, apellido, membresia):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def mostrar_datos(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Membresía: {self.membresia}")







