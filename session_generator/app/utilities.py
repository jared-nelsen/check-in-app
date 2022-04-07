import dateutil.parser
from datetime import datetime, timedelta

def liesWithinNextHour(check_in_time):
    # Convert the ISO8601 string to a date
    check_in_time = dateutil.parser.parse(check_in_time)
    # Define now
    now = datetime.now()
    # Define an hour from now
    an_hour_from_now = now + timedelta(hours=1)
    # Detect if the check in time lies between now and an hour from now
    if check_in_time >= now and check_in_time <= an_hour_from_now:
        return True
    else:
        return False