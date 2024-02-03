from datetime import datetime, tzinfo
import pytz


melbourne = pytz.timezone('Australia/Melbourne')

if __name__ == "__main__":
    input_time = input('Enter the time: ')
    input_time_zone = input('Enter the time zone: ')
    time_object = datetime.strptime(input_time, '%H:%M')