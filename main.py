import discord
import os
from commands import createReminder, listUserReminders, lolMessage
from keep_alive import keep_alive
from routines import ReminderBot

# instantiate discord client
client = discord.Client()

# discord event to check when the bot is online
@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message):
    if message.content.startswith('!reminder ') or message.content.startswith('!remind '):
        await createReminder(message)
    elif message.content == '!reminders':
        await listUserReminders(message)
    elif "penis" in message.content.lower() and message.author.bot != True:
        await lolMessage(message)

client.loop.create_task(ReminderBot(client))

keep_alive()  # keep web server alive

# get bot token from .env and run client
# has to be at the end of the file
client.run(os.getenv('TOKEN'))
