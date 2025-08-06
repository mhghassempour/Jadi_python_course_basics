import datetime

birthdate = datetime.datetime(1999,11,12)
now = datetime.datetime.now()
sen = now - birthdate
print(sen)
years_old = int(sen.days/365)
hours_old = int(sen.seconds/3600)
minutes_old = int((sen.seconds - hours_old *3600)/60)
seconds_old = int((sen.seconds - hours_old *3600 - minutes_old *60))
print(f'you are {years_old} years and {sen.days - years_old*365} days and {hours_old} hours'
      f'and {minutes_old} minutes and {seconds_old} seconds  old')
