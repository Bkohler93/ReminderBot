from replit import db
from datetime import timedelta
from utils import getTime, formatTime

class Database:
    def __init__(self):
        self.db = db

    def keys(self):
        return self.db.keys()

    def reset(self):
        for key in self.keys():
            self.delete_by_key(key)

    def cleanup(self):
        now = getTime("US/Mountain")
        now -= timedelta(seconds=2)  # allow extra time for reminders to pop up
        nowStr = formatTime(now)

        for key in self.keys():
            if nowStr > key:
                self.delete_by_key(key)

    def search_by_prefix(self, prefix=""):
        return self.db.prefix(prefix)

    def delete_by_key(self, key=""):
        if key:
            del db[key]

    def get_current_reminders(self):
        now = getTime("US/Mountain")
        nowStr = formatTime(now)
        matches = self.search_by_prefix(nowStr)

        reminders = []

        for match in matches:
            db_match = db[match]
            reminders.append(
                {
                    "message": db_match["message"],
                    "authorId": str(db_match["authorId"]),
                    "time": match,
                    "author": db_match["author"],
                    "channelId": db_match["channelId"],
                }
            )

            self.delete_by_key(match)

        return reminders

    def get_users_reminders(self, authorId):
        now = getTime("US/Mountain")
        nowStr = formatTime(now)

        reminders = []

        if not authorId:
            return reminders

        for key in self.keys():
            db_item = db[key]

            if db_item["authorId"] == authorId and key > nowStr:
                reminders.append({"message": db_item["message"], "time": key})

        return reminders

class Reminder:
  def __init__(self, author=None, message="", channel=None):
    self.db = Database()
    self.author = author
    self.message = message
    self.channel = channel

  @property
  def is_valid(self):
    if (
      self.author and 
      (self.message and self.message.strip() != "") and 
      self.channel
    ):
      return True

    return False

  def get_db_data(self):
    return {
      'authorId': self.author.id,
      'message': self.message,
      'author': self.author,
      'channelId': self.channel.id      
    }

  def save(self, time):
    if not self.is_valid:
      return None

    reminder_to_save = self.get_db_data()

    self.db[time] = reminder_to_save

    return reminder_to_save
