from pyrogram import Client

api_id = input("Enter API_ID:14812855\n")
api_hash = input("Enter API_HASH:6a886e99b9699f9f876503fb4ac7df7d\n")
bot_token = input("Enter BOT_TOKEN:5349526620:AAGCVZnwC0WBIWn_sVGToIFU4IeoD46UoXQ\n")

client = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
client.start()

print("Session String:\n")
print(client.export_session_string())
