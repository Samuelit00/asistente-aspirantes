import httpx
from app.config import BOT_TOKEN, WEBHOOK_SECRET;


def set_webhook():
    payload = {
        "url": "https://restaurant-relief-enzyme-eds.trycloudflare.com/webhook",
        "secret_token": WEBHOOK_SECRET
    }
    respuesta = httpx.post(f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook', json=payload)
    return respuesta.status_code

def send_message(chat_id: int, text: str):
    payload = {
        "chat_id": chat_id,
        "text": text

    }
    respuesta = httpx.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage', json=payload, timeout=7)
    return respuesta.status_code










