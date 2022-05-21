from datetime import datetime, timedelta

print(f'time of now: {datetime.now()}')  # current time
#print(datetime.utcnow()) # global time

# time delta inputs
# days=0, seconds=0, microseconds=0, miliseconds-0, minutes=0, hours=0, weeks=0

print(datetime.now() - timedelta(days=1)) # it prints time of 1 day ago
print(datetime.now() - timedelta(minutes=1))  # it prints time of 1 minute ago
print(datetime.now() - timedelta(weeks=1))  # it prints time of 1 week ago

print('-------------------------------------')

twenty_six_years_ago = datetime.now() - timedelta(days= 26 * 365)
print(twenty_six_years_ago)

twenty_six_years_ago2 = datetime(year=2012, month=3, day=2)
print(twenty_six_years_ago2)

print('------------------------------------------')

yesterday = datetime.now() - timedelta(days=1)
now = datetime.now()

print(now - yesterday)

print((now - yesterday).days)

print((now - twenty_six_years_ago).days // 365)

