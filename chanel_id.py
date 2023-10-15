from telethon import TelegramClient, events
import asyncio
api_id = '20796854'
api_hash = '26b5566d9211aae142762032996ca30e'
client = TelegramClient('none', api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
        async for dialog in client.iter_dialogs():
          if dialog.is_channel:
           print(f'{dialog.id}:{dialog.title}')

client.start()
client.run_until_disconnected()
