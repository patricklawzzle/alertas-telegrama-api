from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "7979851171:AAHPDWvBiQmYomCPfddEVGzjHsVlluKA-w0"
CHAT_ID = "723000185"

@app.post("/alerta")
async def recibir_alerta(request: Request):
    data = await request.json()
    mensaje = data.get("mensaje", "⚠️ No se recibió mensaje")
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    requests.post(telegram_url, data=payload)
    return {"status": "ok", "mensaje": mensaje}
