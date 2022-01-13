import discord
import os
from commands import COMMAND_LIST
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
    command = COMMAND_LIST.match(message.content)
    if command:
        await command.exec(message)

client.loop.create_task(ReminderBot(client))

keep_alive()  # keep web server alive

# get bot token from .env and run client
# has to be at the end of the file
client.run(os.getenv('TOKEN'))
