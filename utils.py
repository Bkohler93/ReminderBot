from datetime import datetime, timedelta
from pytz import timezone, utc
import re

DEFAULT_TIMEZONE = 'US/Mountain'

def setRemindTime(times):
    now = getTime(DEFAULT_TIMEZONE)
    for t in times:
        timeUnit = re.search('[ymwdhMs]', t).group()
        amount = int(re.search("[1-9][0-9]*", t).group())

        if (timeUnit == 'y'):
            now += timedelta(years=amount)
        if (timeUnit == 'M'):
            now += timedelta(months=amount)
        if (timeUnit == 'w'):
            now += timedelta(weeks=amount)
        if (timeUnit == 'd'):
            now += timedelta(days=amount)
        if (timeUnit == 'h'):
            now += timedelta(hours=amount)
        if (timeUnit == 'm'):
            now += timedelta(minutes=amount)
        if (timeUnit == 's'):
            now += timedelta(seconds=amount)

    remindTime = now.replace(microsecond=0)
    return remindTime

def getTime(tzone):
  now = datetime.now(tz=utc)
  now = now.astimezone(timezone(tzone))
  return now

def formatTime(time):
  timeFormatted = time.strftime("%Y-%m-%d %H:%M:%S")

  return timeFormatted
