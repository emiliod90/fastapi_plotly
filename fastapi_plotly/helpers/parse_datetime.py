import ciso8601
import time
import datetime


def convert_datetime(date):
    return ciso8601.parse_datetime(date)


def subtract_date(date_time, days):
    return date_time - datetime.timedelta(days)


def convert_to_unix(date_time):
    return int(time.mktime(date_time.timetuple()))


def format_time(time):
    return datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d')
