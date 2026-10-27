# Sistema Zona Fit

Proyecto de aprendizaje en Python con conexión a MySQL mediante un pool.

## Configuración

1. Instala el conector: `python -m pip install mysql-connector-python`.
2. Copia `config.example.json` como `config.local.json` y escribe tu contraseña de MySQL.
3. Revisa el usuario, servidor, puerto y nombre de la base en `conexión.py`.
4. Ejecuta `python conexión.py` para probar la conexión.

La base utilizada es `zona_fit`, con la tabla `clientes`. La base y sus datos se administran por separado en MySQL.

`config.local.json` queda excluido de Git. No publiques tus credenciales.

Ejecuta `python main.py` para listar, agregar, modificar y eliminar clientes en MySQL.
