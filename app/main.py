from fastapi import FastAPI
from pydantic import BaseModel
from app.telegram import send_message, set_webhook
# Creación de la aplicación FastAPI
app = FastAPI()
set_webhook()
@app.get("/")
def raiz_royecto():
    return { "mensaje": "Funcionamiento correcto de la aplicación FastAPI" }


@app.post("/webhook")
def recibir_update(payload: dict):
    # Recibimiento de todos los parametros del mensaje enviado por el usuario
    id_update = payload.get("update_id")
    id_message = payload.get("message", {}).get("message_id")
    id_chat = payload.get("message",{}).get("chat",{}).get("id")
    text_message = payload.get("message", {}).get("text")
    #Confirmación de recibido de mensaje y respuesta del mismo con POST a telgram
    if id_chat is not None and text_message is not None:
        send_message(id_chat, text_message)
    elif id_chat is not None:
        send_message(id_chat,"En este momento solo se aceptan mensajes de texto")
    return {"ok": True}