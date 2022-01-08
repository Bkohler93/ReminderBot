from datetime import datetime, timedelta
import re

def setRemindTime(times):
    now = datetime.now()

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