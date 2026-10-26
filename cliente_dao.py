

from cliente import Cliente
from conexión import obtener_conexion

clientes = [
    Cliente(1, "Carlos", "Pérez", "Black"),
    Cliente(2, "Carla", "Pérez", "Standard")
]

def listar_clientes():
    for cliente in clientes:
        cliente.mostrar_datos()
        print()

def agregar_cliente():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    membresia = input("Introduzca la membresía: ")

    nuevo_id = max((cliente.id for cliente in clientes), default=0) + 1

    nuevo_cliente = Cliente(nuevo_id, nombre, apellido, membresia)

    clientes.append(nuevo_cliente)

    print("Cliente agregado correctamente.")

def modificar_cliente():
    id_cliente = int(input("Ingrese el ID del cliente: "))

    for cliente in clientes:
        if cliente.id == id_cliente:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_apellido = input("Ingrese el nuevo apellido: ")

            cliente.nombre = nuevo_nombre
            cliente.apellido = nuevo_apellido

            print("Nombre modificado correctamente.")
            break
        
    else:
            print("No existe el usuario con ID solicitado")


def eliminar_cliente():
    id_cliente = int(input("Ingrese el ID del cliente que desea eliminar: "))

    for cliente in clientes:
        if cliente.id == id_cliente:
            clientes.remove(cliente)
            print("Cliente eliminado correctamente")
            break
    else:
        print("No existe un cliente con ese ID")
