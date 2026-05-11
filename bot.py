import telebot
import os
import random
from flask import Flask
from threading import Thread

# --- FLASK SERVER PARA SA RENDER ---
app = Flask('')
@app.route('/')
def home():
    return "Shark Engine is Online!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

# --- BOT SETUP ---
# Siguraduhin na 'BOT_TOKEN' ang nasa Render Environment Variables mo
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: "vs" in message.text.lower())
def handle_prediction(message):
    try:
        teams = message.text.lower().split("vs")
        t1 = teams[0].strip().upper()
        t2 = teams[1].strip().upper()

        # Strategy Simulation
        pub = random.randint(65, 82)
        shark = random.randint(58, 76)
        
        res = (f"🦈 <b>SHARK STRATEGY ENGINE</b>\n"
               f"🥊 <b>{t1} vs {t2}</b>\n"
               f"───────────────────\n\n"
               f"📊 <b>ESTIMATED MARKET SPLIT:</b>\n"
               f"👥 Public Volume: <b>{pub}%</b>\n"
               f"🐋 Shark Handle: <b>{shark}%</b>\n\n"
               f"🎯 <b>SHARK MOVE:</b>\n"
               f"✅ <b>STRATEGY:</b> Backing the Sharp Money Flow.\n"
               f"📈 <b>CONFIDENCE:</b> Medium-High\n\n"
               f"💡 <i>Tip: Check Action Network for real-time handle discrepancy.</i>")
        
        bot.reply_to(message, res, parse_mode="HTML")
    except Exception:
        bot.reply_to(message, "❌ Use: Team A vs Team B")

if __name__ == "__main__":
    # Start Flask in a separate thread
    t = Thread(target=run_flask)
    t.start()
    
    # Start Telegram Bot
    bot.remove_webhook()
    bot.polling(none_stop=True)
