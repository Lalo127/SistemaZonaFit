# pooling permite mantener varias conexiones listas para usar.
# Error permite detectar errores que vienen de MySQL.
import json
from pathlib import Path
from mysql.connector import pooling, Error

# La contraseña se guarda en un archivo local que Git ignora.
with Path(__file__).with_name("config.local.json").open(encoding="utf-8") as archivo:
    configuracion = json.load(archivo)

# Reunimos aquí la configuración y las funciones de conexión a MySQL.
class Conexion:
    # Datos para encontrar la base de datos e iniciar sesión.
    # DATABASE: nombre de la base que ya existe en MySQL.
    DATABASE = "zona_fit"
    # Usuario y contraseña de MySQL.
    USERNAME = "root"
    PASSWORD = configuracion["password"]
    # Puerto por el que MySQL recibe conexiones (normalmente 3306).
    DB_PORT = 3306
    # localhost significa que MySQL está en esta misma computadora.
    HOST = "localhost"
    # Un pool es un grupo de conexiones que se prestan y se reutilizan.
    # Aquí tendrá 5 conexiones; POOL_NAME es el nombre de ese grupo.
    POOL_SIZE = 5 
    POOL_NAME = "zona_fit_pool"
    # None significa que todavía no hemos creado el grupo.
    pool = None

    # @classmethod permite llamar Conexion.obtener_pool() sin crear un objeto.
    # cls se refiere a la clase Conexion y permite acceder a sus datos.
    @classmethod
    def obtener_pool(cls):
        # Solo creamos el grupo la primera vez que se necesita.
        if cls.pool is None:
            # try intenta ejecutar este código; except atiende un error de MySQL.
            try:
                # Crea el grupo usando los datos definidos arriba.
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )

            except Error as e:
                # e contiene el detalle del error que ocurrió.
                print(f"Ocurrió un error al obtener pool: {e}")
                # Propaga el error para que el programa que llamó sepa que falló.
                raise

        # Devuelve el grupo, tanto si acaba de crearse como si ya existía.
        return cls.pool

    @classmethod
    def obtener_conexion(cls):
        # Obtiene el grupo y pide prestada una conexión para trabajar con MySQL.
        return cls.obtener_pool().get_connection()
    
    @classmethod
    def liberar_conexion(cls,conexion):
        # Al venir de un pool, close() devuelve la conexión al grupo.
        # Así puede reutilizarse en otra consulta.
        conexion.close()

# Esta prueba solo se ejecuta al iniciar este archivo directamente.
# No se ejecuta cuando otro archivo importa la clase Conexion.
if __name__ == "__main__":
    # 1. Crea u obtiene el grupo de conexiones.
    pool = Conexion.obtener_pool()
    # Muestra el objeto pool, no los registros de la base de datos.
    print(pool)
    # 2. Pide prestada una conexión del grupo.
    conexion1 = pool.get_connection()
    print(conexion1)
    # 3. Devuelve la conexión cuando termina de usarla.
    Conexion.liberar_conexion(conexion1)
    print(f"Se ha liberado el objeto de conexión")
    
