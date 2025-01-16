# A structured workflow tailored to EthioMart project for fine-tuning Amharic NER models. Here’s a breakdown of the pipeline with coding support for each step.
# 1. Data Ingestion Pipeline
# Objective: Fetch data from Telegram channels and preprocess it.
# Libraries/Tools: telethon (for Telegram scraping), pandas, re.

from telethon.sync import TelegramClient
import pandas as pd
import re
import os

# Configure Telegram API credentials
api_id = os.getenv("TELEGRAM_API_ID") or '21483974'
api_hash = os.getenv("TELEGRAM_API_HASH") or 'ecf78ee84312a3e7368578e5e29da1f8'
phone = os.getenv("TELEGRAM_PHONE") or '251911699986'

# Connect to Telegram client
client = TelegramClient(phone, api_id, api_hash)
client.start()

print("Client connected successfully!")

# Fetch messages from a channel
<<<<<<< HEAD
def fetch_channel_data(channel_username, limit=50):
=======
def fetch_channel_data(channel_username, limit=100):
>>>>>>> 8af4ca7cedebb665f282e8733b0214fb141b6adf
    messages = []
    for message in client.iter_messages(channel_username, limit=limit):
        if message.text:
            messages.append({'text': message.text, 'date': message.date, 'sender': message.sender.username})
    return pd.DataFrame(messages)

# Preprocess text
def preprocess_amharic_text(df):
    # Tokenize and clean text
    df['clean_text'] = df['text'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    return df

# Fetch data from Telegram channel
<<<<<<< HEAD
channel_data = fetch_channel_data('meneshayeofficial')
=======
channel_data = fetch_channel_data('shegershoes123')
>>>>>>> 8af4ca7cedebb665f282e8733b0214fb141b6adf

# Preprocess data
clean_data = preprocess_amharic_text(channel_data)

# Save data to CSV
<<<<<<< HEAD
clean_data.to_csv(r'C:\Users\Almazt\OneDrive - Ethiopian Airlines\Desktop\10 Academy\EthioMart-Week 5\data/telegram_meneshayeofficial_clean_data.csv', index=False)
=======
clean_data.to_csv('telegram_data.csv', index=False)
>>>>>>> 8af4ca7cedebb665f282e8733b0214fb141b6adf

# Disconnect from Telegram client
client.disconnect()