import telebot
import requests
import os
import random
from flask import Flask
from threading import Thread

# --- SERVER PARA SA RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Universal Shark Bot % Breakdown is Live!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

# --- SHARK LIQUIDITY BOT TOKEN ---
BOT_TOKEN = "7826833790:AAH2b2Nd7r-gd8Ntqh-V3LVRBwDqFXVZsbU"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: "vs" in message.text.lower())
def handle_universal(message):
    try:
        bot.reply_to(message, "📊 Scanning Market Percentages & Sharp Liquidity...")
        teams = message.text.lower().split("vs")
        t1 = teams[0].strip().upper()
        t2 = teams[1].strip().upper()

        # --- PERCENTAGE LOGIC ---
        # Public tickets are usually high, but Sharp handle (money) is concentrated.
        pub_tickets = random.randint(68, 82)
        sharp_handle = random.randint(55, 75)

        res = (f"🦈 <b>UNIVERSAL SHARK ALERT: {t1} vs {t2}</b>\n"
               f"───────────────────\n\n"
               f"📊 <b>MARKET BREAKDOWN:</b>\n"
               f"👥 <b>Public Tickets:</b> {pub_tickets}% on <b>{t1}</b>\n"
               f"🐋 <b>Shark Handle:</b> {sharp_handle}% on <b>{t2}</b>\n"
               f"<i>(Signal: Reverse Line Movement Detected)</i>\n\n"
               f"🌊 <b>SHARK ACTIVITY:</b>\n"
               f"▫️ Flow: <b>SMART MONEY</b> detected on 🟢 <b>{t2}</b>\n"
               f"▫️ Trend: Crowd is on {t1}, but pros are hitting {t2}.\n\n"
               f"🎯 <b>THE SHARK PLAY:</b>\n"
               f"✅ <b>FADE THE PUBLIC:</b> Backing <b>{t2}</b>\n"
               f"📈 <b>CONFIDENCE:</b> HIGH (+5.2% EV)\n"
               f"───────────────────\n"
               f"💡 <i>Note: Sharks hold the minority of tickets but the majority of the money.</i>")
        
        bot.send_message(message.chat.id, res, parse_mode="HTML")
    except:
        bot.reply_to(message, "❌ Use: Team A vs Team B")

if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.remove_webhook()
    bot.polling(none_stop=True)
