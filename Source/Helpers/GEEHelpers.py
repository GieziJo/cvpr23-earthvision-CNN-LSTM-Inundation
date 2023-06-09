import datetime

def GetDateFromGEETimeStamp(timeStamp):
    return datetime.datetime.fromtimestamp(timeStamp / 1000.0, tz=datetime.timezone.utc)

def GetGEETimeStampFromDate(year,month,day):
    return int(datetime.datetime.timestamp(datetime.datetime(year,month,day)) * 1000)