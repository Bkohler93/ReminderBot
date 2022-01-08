from db import getCurrentReminders
import asyncio


async def ReminderBot(client):

    await client.wait_until_ready()
    channel = client.get_channel(id=928923454495940689)
    while not client.is_closed():

        matches = getCurrentReminders()

        for match in matches:
            print("Event happening now")
            ttsRes = "Smack! Hey bitch, remember " + match['message']
            textRes = "Thanks for the reminder <@" + match[
                'authorId'] + "> | Set at " + match['time']

            await channel.send(ttsRes, tts=True)
            await channel.send(textRes)
            # await channel.send("<@&490351249317822464> " + textRes)

        await asyncio.sleep(0.5)
