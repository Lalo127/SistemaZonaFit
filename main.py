

from cliente_dao import listar_clientes, agregar_cliente, modificar_cliente, eliminar_cliente


def Menu_de_opciones():

    while True:

        print(f"\n====SISTEMA DE ZONA FIT===")
        print(f"1. Listar clientes")
        print(f"2. Agregar Cliente")
        print(f"3. Modificar Cliente")
        print(f"4. Eliminar Cliente")
        print(f"5. Salir")

        opcion = input(f"Selecciones una opción: ")


        if opcion == "1":
            listar_clientes() 
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print(f"Saliendo del sistema...")
            break

        else:
            print(f"Opción no Válida intente de nuevo")



Menu_de_opciones()

