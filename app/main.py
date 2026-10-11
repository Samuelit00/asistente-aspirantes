from fastapi import FastAPI
from pydantic import BaseModel
# Creación de la aplicación FastAPI
app = FastAPI()

@app.get("/")
def raiz_royecto():
    return { "mensaje": "Funcionamiento correcto de la aplicación FastAPI" }


@app.post("/webhook")
def recibir_update(payload: dict):
    id_update = payload.get("update_id")
    id_message = payload.get("message", {}).get("message_id")
    text_message = payload.get("message", {}).get("text")
    print(f"Update ID: {id_update}, Message ID: {id_message}, Text: {text_message}")
    return {
        "update_id": id_update,
        "message_id": id_message,
        "text": text_message
    }