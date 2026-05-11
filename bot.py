import telebot
import os
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Shark Insider Engine is Online!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome = (f"🦈 <b>WELCOME TO SHARK INSIDER</b>\n\n"
               f"Dito tayo kukuha ng <b>REAL DATA</b>. Gamitin ang format:\n"
               f"👉 <code>Team A vs Team B</code>\n\n"
               f"Ibibigay ko sa'yo ang direct link sa market para makita ang <b>True Shark Money.</b>")
    bot.reply_to(message, welcome, parse_mode="HTML")

@bot.message_handler(func=lambda message: "vs" in message.text.lower())
def handle_shark_links(message):
    try:
        teams = message.text.lower().split("vs")
        t1 = teams[0].strip().upper()
        t2 = teams[1].strip().upper()

        # Direct Links para sa Real Data
        nba_link = "https://www.actionnetwork.com/nba/public-betting"
        mlb_link = "https://www.actionnetwork.com/mlb/public-betting"
        soccer_link = "https://www.actionnetwork.com/soccer/public-betting"

        res = (f"🚀 <b>SHARK INSIDER REPORT: {t1} vs {t2}</b>\n"
               f"───────────────────\n\n"
               f"🔗 <b>GET REAL-TIME DATA HERE:</b>\n"
               f"🏀 <a href='{nba_link}'>NBA Public vs Money %</a>\n"
               f"⚾ <a href='{mlb_link}'>MLB Public vs Money %</a>\n"
               f"⚽ <a href='{soccer_link}'>Football/Soccer Data</a>\n\n"
               f"🧠 <b>SHARK READING GUIDE:</b>\n"
               f"1️⃣ Tingnan ang <b>'Money %'</b> vs <b>'Bets %'</b>.\n"
               f"2️⃣ Kapag ang Money % ay <b>MAS MATAAS</b> kaysa Bets %, nandoon ang mga <b>SHARKS (Whales)</b>. 🐋\n"
               f"3️⃣ Kapag ang Bets % ay sobrang taas (80%+) pero ang Money % ay mababa, iwasan mo 'yun—<b>Public Trap</b> 'yun. 👥\n\n"
               f"🎯 <b>STAKING ADVICE:</b>\n"
               f"Kung ang Sharks ay nasa Underdog, magandang <b>Value Play</b> 'yan. Gamitin ang 1-2% bankroll units.")

        bot.reply_to(message, res, parse_mode="HTML", disable_web_page_preview=True)
    except:
        bot.reply_to(message, "❌ Format: Team A vs Team B")

if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.remove_webhook()
    bot.polling(none_stop=True)
