from telethon.sync import TelegramClient
from datetime import datetime, timedelta, timezone

import settings

api_id = settings.API_ID
api_hash = settings.API_HASH
phone_number = settings.PHONE_NUMBER

# create a TelegramClient instance
client = TelegramClient('account', settings.API_ID, settings.API_HASH)

# connect and log in
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))


# get today messages from target tg channel (channels or chats which your account can read)
def get_today_message(channel_username):
    start_of_current_day = datetime.now(tz=timezone.utc) - timedelta(hours=datetime.now().hour)
    return client.iter_messages(channel_username, offset_date=start_of_current_day, reverse=True, limit=2000)


# sending our post (digest) to target channel
def send_post(post):
    client.send_message(settings.DIGEST_CHANNEL, post)


# USE ONLY WHEN YOU ARE PLANNING EXIT FROM PROGRAM, logout from telegram account
def log_out():
    client.log_out()
