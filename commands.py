import re
from utils import setRemindTime
from db import setReminder, getUserReminders

async def createReminder(message):
  times = re.findall("[1-9][0-9]*[ymwdhMs]+", message.content)

  if len(times) < 1:
      await message.author.send(
          "Invalid format. Use '!reminder [time til reminder] [message]'"
      )
      await message.author.send(
          "Here is an example to set a reminder for 3 hours and 15 minutes from now:"
      )
      await message.author.send("!reminder 3h15m hello world")
      return

  textMessage = ' '.join(
  message.content.split()[2:])
  remindTime = setRemindTime(times)
  formattedTime = remindTime.strftime("%Y-%m-%d %H:%M:%S")
  setReminder(formattedTime, message.author.id, textMessage)

  await message.channel.send(f"Reminder set for {formattedTime}")

async def listUserReminders(message):

  reminders = getUserReminders(message.author.id)
  
  await message.channel.send("You have {length} {reminderS} scheduled <@{id}>:".format(reminderS="reminders" if len(reminders) > 1 else "reminder", length = len(reminders), id=message.author.id))

  for reminder in reminders:
    await message.channel.send(f"{reminder['message']} | {reminder['time']}")
  