import telebot
import os
import random
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Shark Strategy Engine is Online!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: "vs" in message.text.lower())
def handle_strategy(message):
    try:
        teams = message.text.lower().split("vs")
        t1 = teams[0].strip().upper()
        t2 = teams[1].strip().upper()

        # Random Strategy Simulation (Base sa Shark Theory)
        pub_vol = random.randint(65, 85)
        shark_handle = random.randint(55, 75)
        
        res = (f"🦈 <b>SHARK STRATEGY SCANNER</b>\n"
               f"🥊 <b>{t1} vs {t2}</b>\n"
               f"───────────────────\n\n"
               f"📊 <b>THEORETICAL MARKET SPLIT:</b>\n"
               f"👥 Public Volume: {pub_vol}%\n"
               f"🐋 Shark Handle: {shark_handle}%\n\n"
               f"🎯 <b>SHARK MOVE:</b>\n"
               f"✅ <b>ACTION:</b> Fade the Public flow.\n"
               f"📈 <b>CONFIDENCE:</b> Medium-High\n\n"
               f"💡 <i>Tip: Check Action Network for real-time handle discrepancy before placing bets.</i>")
        
        bot.reply_to(message, res, parse_mode="HTML")
    except:
        bot.reply_to(message, "❌ Use: Team A vs Team B")

if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.remove_webhook()
    bot.polling(none_stop=True)
