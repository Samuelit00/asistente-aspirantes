import os
from dotenv import load_dotenv
from pathlib import Path


# Cargar variables de entorno desde el archivo .env
ruta_base = Path(__file__).resolve().parent.parent
ruta_env = ruta_base / '.env'

load_dotenv(dotenv_path=ruta_env)


def verificar_variable_entorno(var : str):
    variable = os.environ.get(var)
    if variable is None:
        raise ValueError(f"La variable de entorno {var} no está definida. Asegúrate de tener un archivo .env con la variable correspondiente.")
    return variable

BOT_TOKEN = verificar_variable_entorno("TELEGRAM_BOT_TOKEN")
WEBHOOK_SECRET = verificar_variable_entorno("TELEGRAM_WEBHOOK_SECRET")
