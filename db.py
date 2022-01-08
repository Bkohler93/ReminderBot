from replit import db
from datetime import datetime, timedelta

def setReminder(timeStr, authorId, textMessage):
  db[timeStr] = {
      'author': authorId,
      'message': textMessage
  }

def getCurrentReminders():
  now = datetime.now()
  
  matches = db.prefix(now.strftime("%Y-%m-%d %H:%M:%S"))

  reminders = []
  for match in matches:
    
    reminders.append({
      'message': db[match]['message'],
      'authorId': str(db[match]['author']),
      'time': match
      })

    del db[match]

  return reminders

def cleanup():
  now = datetime.now()
  now -= timedelta(seconds = 5) #allow extra time for reminders to pop up
  nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
  
  for key in db.keys():
    if nowStr > key:
        del db[key]

def reset():
  for key in db.keys():
    del db[key]
    
def getUserReminders(authorId):

  now = datetime.now()
  nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
  reminders = []
  for key in db.keys():
    
    if 
    if db[key]['author'] == authorId and key > nowStr:
      reminders.append({
        'message': db[key]['message'],
        'time': key
      })
  return reminders