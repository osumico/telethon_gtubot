from telethon.sync import TelegramClient, events # 1.14.0
from googletrans import Translator # 3.1.0a0
import json
import os

with open(f'{os.getcwd()}\\api.json') as json_file:
    key = json.load(json_file) # You need to replace in the ID/Hash file with your's
    json_file.close()
    
API_ID, API_HASH = key["id"], key["hash"]
APP_NAME = "wizsia"

with TelegramClient(APP_NAME, API_ID, API_HASH) as client:
    gt = Translator()
    
    
    @client.on(events.NewMessage(pattern='!"*'))
    async def handler(event):
        cht_id = event.message.peer_id.user_id
        msg = event.message.message.split('!"')[1]
        
        await event.message.delete()
        await client.send_message(cht_id, gt.translate(msg, dest='en').text)

    client.run_until_disconnected()
