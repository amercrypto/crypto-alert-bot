import os
import time
import requests
import logging
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=BOT_TOKEN)

def send_alert(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        logging.error(f"Failed to send message: {e}")

def check_market():
    send_alert("🚀 فرصة سكالب: WIF وصلت دعم مهم، راقب الدخول الآن!")

if __name__ == "__main__":
    while True:
        check_market()
        time.sleep(3600)
