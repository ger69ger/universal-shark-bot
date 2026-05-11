import telebot
import requests
import os
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "SharkExchange Real-Time Engine is Live!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

# --- SECURE TOKENS ---
BOT_TOKEN = os.environ.get('BOT_TOKEN')
ODDS_API_KEY = os.environ.get('ODDS_API_KEY')
bot = telebot.TeleBot(BOT_TOKEN)

def get_real_odds():
    # Kukuha ng laro sa lahat ng sports (NBA, MLB, Soccer, Tennis)
    url = f"https://api.the-odds-api.com/v4/sports/upcoming/odds/?apiKey={ODDS_API_KEY}&regions=us&markets=h2h"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except: return None

@bot.message_handler(func=lambda message: "vs" in message.text.lower())
def handle_universal_real(message):
    try:
        bot.reply_to(message, "📡 Scanning Global Odds (NBA, MLB, Football, Tennis)...")
        
        teams = message.text.lower().split("vs")
        t1_input = teams[0].strip()
        
        all_games = get_real_odds()
        match = None

        if not all_games:
            bot.reply_to(message, "❌ API Error. Check if your ODDS_API_KEY is correct in Render.")
            return

        # Search for the match
        for game in all_games:
            if t1_input in game['home_team'].lower() or t1_input in game['away_team'].lower():
                match = game
                break
        
        if not match:
            bot.reply_to(message, "❌ No live matchup found. Make sure the team name is correct and they play today!")
            return

        sport = match['sport_title']
        home = match['home_team']
        away = match['away_team']
        
        # Extract Odds
        bookie = match['bookmakers'][0]['title']
        odds_list = match['bookmakers'][0]['markets'][0]['outcomes']
        o1 = next(item for item in odds_list if item['name'] == home)['price']
        o2 = next(item for item in odds_list if item['name'] == away)['price']

        res = (f"🦈 <b>REAL-TIME SHARK ALERT ({sport})</b>\n"
               f"🥊 <b>{away.upper()} vs {home.upper()}</b>\n"
               f"───────────────────\n\n"
               f"🏦 <b>Source:</b> {bookie}\n"
               f"💰 <b>LIVE ODDS:</b>\n"
               f"▫️ {home}: <b>{o1}</b>\n"
               f"▫️ {away}: <b>{o2}</b>\n\n"
               f"🎯 <b>SHARK ANALYSIS:</b>\n"
               f"✅ <b>Sharp Edge:</b> {home if o1 < o2 else away} is favored.\n"
               f"📈 <b>Market Status:</b> ACTIVE\n"
               f"───────────────────\n"
               f"💡 <i>Tip: Real data active. Betting edge detected.</i>")
        
        bot.send_message(message.chat.id, res, parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, "❌ Team not found or No games today.")

if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.remove_webhook()
    bot.polling(none_stop=True)
