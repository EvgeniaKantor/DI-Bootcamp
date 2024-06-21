import datetime

#Ex-4
def display_current_date():
    current_date = datetime.datetime.now()
    print("Current Date:", current_date.date())  # Extract only the date from datetime object
    return current_date

#display_current_date()

#EX-5
def display_amount_of_time_to_new_year(current_date):
    next_year = datetime.datetime(current_date.year + 1, 1, 1)
    time_difference = next_year - current_date
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f'the 1st of January is in {days} and {hours:02}:{minutes:02}:{seconds:02}')

current_date = display_current_date()
display_amount_of_time_to_new_year(current_date)

#Ex-6
def minutes_lived(birthdate, current_date):
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    time_difference = current_date - birthdate
    minutes = int(time_difference.total_seconds() / 60)
    return minutes

birthdate = '1984-11-08'
total_minutes = minutes_lived(birthdate, current_date)
print(f'You have lived {total_minutes} minutes')
