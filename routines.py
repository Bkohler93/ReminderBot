from db import getCurrentReminders, cleanupDb
from discord import Embed
import asyncio

async def ReminderBot(client):

    await client.wait_until_ready()
    
    while not client.is_closed():

        matches = getCurrentReminders()

        for match in matches:
            
            channel = client.get_channel(id=match['channelId'])
            msg = "Hey bitch, remember {reminder}".format(reminder=match['message'])
            embedVar = Embed(title="SMACK!", description=msg)
            embedVar.set_footer(text="Thanks for the reminder {author}\t\t\t\t created at {time} MST".format(author=match['author'], time=match['time']))

            print("Event happening now")
            tts = await channel.send("Hey bitch", tts=True)
            await channel.send(embed = embedVar)
            await asyncio.sleep(2)
            await tts.delete()

        await asyncio.sleep(0.5)
        
        

async def cleanDatabase(client):
  await client.wait_until_ready()
  while not client.is_closed():
    cleanupDb()
    await asyncio.sleep(300)