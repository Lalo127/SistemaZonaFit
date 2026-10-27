# Corrección: importamos desde conexión.py, que está en esta misma carpeta.
from conexión import Conexion
from cliente import Cliente


# El DAO se encarga de leer y guardar clientes en MySQL.
class ClienteDAO:
    # Correcciones: la tabla es clientes, la columna es membresia
    # y para ordenar se escribe ORDER BY. Indicamos las columnas en orden.
    SELECCIONAR = "SELECT id, nombre, apellido, membresia FROM clientes ORDER BY id"
    # Los %s son espacios para valores que el conector envía de forma segura.
    INSERTAR = "INSERT INTO clientes(nombre, apellido, membresia) VALUES(%s, %s, %s)"
    # Corrección: el nombre de la constante es ACTUALIZAR.
    ACTUALIZAR = "UPDATE clientes SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM clientes WHERE id=%s"

    # cls representa esta clase; podemos llamar ClienteDAO.seleccionar().
    @classmethod
    def seleccionar(cls):
        # Corrección: inicializamos ambos recursos por si algo falla al crearlos.
        conexion = None
        cursor = None
        try:
            # Pedimos una conexión prestada al pool.
            conexion = Conexion.obtener_conexion()
            # El cursor permite ejecutar SQL y recoger los resultados.
            cursor = conexion.cursor()
            # Corrección: el try ya contiene el código de la consulta.
            cursor.execute(cls.SELECCIONAR)
            # fetchall() recoge todas las filas que devolvió la consulta.
            registros = cursor.fetchall()
            # Mapeo: convertimos cada fila de MySQL en un objeto Cliente.
            clientes = []
            for registro in registros:
                # Las posiciones coinciden con las columnas del SELECT:
                # 0: id, 1: nombre, 2: apellido, 3: membresia.
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrió un error al seleccionar clientes: {e}')
            # Corrección: propagamos el error para evitar devolver None
            # y que luego falle el for al intentar recorrer los clientes.
            raise
        finally:
            # finally se ejecuta incluso si falla la consulta.
            # Corrección: comprobamos cada recurso antes de cerrarlo.
            try:
                if cursor is not None:
                    cursor.close()
            finally:
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        # El orden de los valores coincide con el orden de los %s del INSERT.
        valores = (cliente.nombre, cliente.apellido, cliente.membresia)
        return cls._ejecutar_cambio(cls.INSERTAR, valores)

    @classmethod
    def actualizar(cls, cliente):
        # El ID al final indica qué cliente se modifica.
        valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
        return cls._ejecutar_cambio(cls.ACTUALIZAR, valores)

    @classmethod
    def eliminar(cls, cliente):
        # La coma crea una tupla con un solo valor: el ID a eliminar.
        return cls._ejecutar_cambio(cls.ELIMINAR, (cliente.id,))

    @classmethod
    def _ejecutar_cambio(cls, consulta, valores):
        # Compartimos estos pasos para insertar, actualizar y eliminar.
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(consulta, valores)
            # commit confirma y guarda el cambio en MySQL.
            conexion.commit()
            # Devolvemos cuántas filas cambiaron para informar al usuario.
            return cursor.rowcount
        except Exception:
            if conexion is not None:
                # Si falla, deshacemos los cambios que no se hayan confirmado.
                conexion.rollback()
            # Dejamos que el menú reciba y muestre el error.
            raise
        finally:
            try:
                if cursor is not None:
                    cursor.close()
            finally:
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)

# Esta prueba solo se ejecuta al iniciar cliente_dao.py directamente.
if __name__ == '__main__':
    # Pedimos la lista de clientes y mostramos cada objeto con su __str__.
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)
