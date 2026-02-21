import MetaTrader5 as mt5
import telebot
import time

TOKEN = "TU_TOKEN_DE_TELEGRAM"
CHAT_ID = "TU_CHAT_ID"

bot = telebot.TeleBot(TOKEN)

if not mt5.initialize():
    print("Error al iniciar MT5")

def enviar_operacion():
    positions = mt5.positions_get()
    if positions:
        for position in positions:
            mensaje = f"""
📈 Nueva Operación Detectada

Símbolo: {position.symbol}
Tipo: {position.type}
Lotes: {position.volume}
Precio: {position.price_open}
Ganancia: {position.profit}
"""
            bot.send_message(CHAT_ID, mensaje)

while True:
    enviar_operacion()
    time.sleep(10)
