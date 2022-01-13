import re
from utils import setRemindTime
from db import database, Reminder
from discord import Embed

class Command:
    def __init__(self, prefix="!", value="", fnc=None):
        self.prefix = prefix
        self.value = value
        self.exec = fnc

    @property
    def is_valid(self):
        if self.prefix and self.exec and (self.value and self.value.strip() != ""):
            return True

        return False

class CommandList:
    def __init__(self, commands=[]):
        self.commands = commands

    @property
    def valid_commands(self):
        valid_commands = []

        for command in self.commands:
            if command.is_valid:
                valid_commands.append(command)

        return valid_commands

    def match(self, text=""):
        matched = None

        for command in self.valid_commands:
            if command.text == text:
                matched = command
                break

        return matched

async def createReminder(message):
  times = re.findall("[1-9][0-9]*[ymwdhMs]+", message.content)

  if len(times) < 1:
    msg = "Invalid format. Use '!reminder [time until reminder] [message]'\nHere is an example to set a reminder for 3 hours and 15 minutes from now.\n!reminder 3h15m hello world"
    await message.author.send(msg)
    return

  textMessage = ' '.join(
  message.content.split()[2:])
  remindTime = setRemindTime(times)
  formattedTime = remindTime.strftime("%Y-%m-%d %H:%M:%S")

  reminder = Reminder(message.author, textMessage, message.channel)
  saved = reminder.save(formattedTime)

  if saved:
    message = f"Reminder set for {formattedTime}"
  else:
    message = "Error setting reminder"

  await message.channel.send(message)

async def listUserReminders(message):
  reminders = database.get_users_reminders(message.author.id)
  description = "{author} has {length} {reminderS} scheduled.".format(
      reminderS="reminders" if len(reminders) != 1 else "reminder",
      length=len(reminders),
      author=message.author.display_name,
  )
  embedVar = Embed(title=description)
  reminderText = ""
  timeStampText = ""
  
  for reminder in reminders:
    reminderText += f"{reminder['message']}\n"
    timeStampText += f"{reminder['time']}\n"

  if (len(reminderText) > 0):
    embedVar.add_field(name="Reminder", value=reminderText, inline=True)
    embedVar.add_field(name="Created At", value=timeStampText, inline=True)
  
  await message.channel.send(embed = embedVar)
  
COMMAND_LIST = CommandList(
    [
        Command("reminder", createReminder),
        Command("remind", createReminder),
        Command("reminders", listUserReminders),
    ]
)