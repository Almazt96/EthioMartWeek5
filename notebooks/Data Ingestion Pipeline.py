# A structured workflow tailored to EthioMart project for fine-tuning Amharic NER models. 
# Here’s a breakdown of the pipeline with coding support for each step.
# 1. Data Ingestion Pipeline
# Objective: Fetch data from Telegram channels and preprocess it.
# Libraries/Tools: telethon (for Telegram scraping), pandas, re.

from telethon.sync import TelegramClient
import pandas as pd
import re
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
phone = os.getenv("TELEGRAM_PHONE")

print(f"API ID: {api_id}")
print(f"API Hash: {api_hash}")
print(f"Phone: {phone}")


# Connect to Telegram client
client = TelegramClient(phone, api_id, api_hash)
client.start()

print("Client connected successfully!")

# Fetch messages from a channel
def fetch_channel_data(channel_username, limit=50):
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
channel_data = fetch_channel_data('meneshayeofficial')

# Preprocess data
clean_data = preprocess_amharic_text(channel_data)

# Save data to CSV
clean_data.to_csv(r'C:\Users\Almazt\OneDrive - Ethiopian Airlines\Desktop\10 Academy\EthioMart-Week 5\data/telegram_meneshayeofficial_clean_data.csv', index=False)

# Disconnect from Telegram client
client.disconnect()