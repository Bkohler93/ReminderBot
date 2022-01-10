from replit import db
from datetime import timedelta
from utils import getTime, formatTime

def setReminder(timeStr, authorId, textMessage, author, channelId):
  db[timeStr] = {
      'authorId': authorId,
      'message': textMessage,
      'author': author,
      'channelId': channelId
  }

def getCurrentReminders():
 
  now = getTime('US/Mountain')
  nowStr = formatTime(now)
  matches = db.prefix(nowStr)

  reminders = []
  for match in matches:
    
    reminders.append({
      'message': db[match]['message'],
      'authorId': str(db[match]['authorId']),
      'time': match,
      'author': db[match]['author'],
      'channelId': db[match]['channelId']
      })

    del db[match]
  
  return reminders

def cleanupDb():
  now = getTime('US/Mountain')
  now -= timedelta(seconds = 2) #allow extra time for reminders to pop up
  nowStr = formatTime(now)
  
  for key in db.keys():
    if nowStr > key:
        del db[key]

def reset():
  for key in db.keys():
    del db[key]
    
def getUserReminders(authorId):
  now = getTime('US/Mountain')
  nowStr = formatTime(now)
  reminders = []
  for key in db.keys():
    
    if db[key]['authorId'] == authorId and key > nowStr:
      reminders.append({
        'message': db[key]['message'],
        'time': key
      })
  
  return reminders