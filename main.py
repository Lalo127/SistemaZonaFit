# Corrección: las funciones antiguas ya no existen; ahora usamos ClienteDAO.
from cliente_dao import ClienteDAO
from cliente import Cliente
from mysql.connector import Error


def Menu_de_opciones():
    # El menú recoge los datos; el DAO ejecuta las consultas en MySQL.
    while True:
        print("\n==== SISTEMA DE ZONA FIT ====")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                clientes = ClienteDAO.seleccionar()
                if not clientes:
                    print("No hay clientes registrados.")
                for cliente in clientes:
                    # print utiliza el método __str__ de Cliente.
                    print(cliente)
            elif opcion == "2":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                membresia = input("Membresía: ")
                # MySQL genera el ID; aquí enviamos los demás datos.
                cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
                ClienteDAO.insertar(cliente)
                print("Cliente agregado correctamente.")
            elif opcion == "3":
                id_cliente = int(input("ID del cliente: "))
                nombre = input("Nuevo nombre: ")
                apellido = input("Nuevo apellido: ")
                membresia = input("Nueva membresía: ")
                cliente = Cliente(id_cliente, nombre, apellido, membresia)
                if ClienteDAO.actualizar(cliente):
                    print("Cliente actualizado correctamente.")
                else:
                    print("No hubo cambios: revisa el ID o si los datos ya eran iguales.")
            elif opcion == "4":
                id_cliente = int(input("ID del cliente que desea eliminar: "))
                if ClienteDAO.eliminar(Cliente(id=id_cliente)):
                    print("Cliente eliminado correctamente.")
                else:
                    print("No existe un cliente con ese ID.")
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            # Evita que el menú se cierre si se escribe texto en lugar de un ID.
            print("El ID debe ser un número entero.")
        except Error as e:
            print(f"No se pudo completar la operación en MySQL: {e}")


# Corrección: importar este archivo no inicia el menú automáticamente.
if __name__ == "__main__":
    Menu_de_opciones()
