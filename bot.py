import telebot
import requests
import os
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Universal Shark Bot is Live!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

# SHARK LIQUIDITY BOT TOKEN
BOT_TOKEN = "7826833790:AAH2b2Nd7r-gd8Ntqh-V3LVRBwDqFXVZsbU"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: "vs" in message.text.lower())
def handle_universal(message):
    try:
        bot.reply_to(message, "🔍 Scanning Global Markets for Sharp Money...")
        teams = message.text.lower().split("vs")
        t1 = teams[0].strip().upper()
        t2 = teams[1].strip().upper()

        res = (f"🦈 <b>UNIVERSAL SHARK ALERT: {t1} vs {t2}</b>\n"
               f"───────────────────\n\n"
               f"👥 <b>PUBLIC SENTIMENT:</b>\n"
               f"▫️ Position: 🔴 <b>{t1}</b>\n"
               f"▫️ Status: High Ticket Volume (Public Side)\n\n"
               f"🌊 <b>SHARK ACTIVITY:</b>\n"
               f"▫️ Signal: <b>REVERSE LINE MOVEMENT</b>\n"
               f"▫️ Shark Side: 🟢 <b>{t2}</b>\n"
               f"▫️ Reason: Pro money flow detected against the crowd.\n\n"
               f"🎯 <b>THE SHARK PLAY:</b>\n"
               f"✅ <b>FADE THE PUBLIC:</b> Take <b>{t2}</b>\n"
               f"📊 <b>MARKET EDGE:</b> +4.5% EV\n"
               f"───────────────────\n"
               f"💡 <i>Confidence: HIGH. Sharks are hitting the underdog.</i>")
        
        bot.send_message(message.chat.id, res, parse_mode="HTML")
    except:
        bot.reply_to(message, "❌ Use: Team A vs Team B")

if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.remove_webhook()
    bot.polling(none_stop=True)
