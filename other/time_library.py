import time
print('time.ctime(0): ', time.ctime(0)) #refrence time
print("*********************\n")

print('time.time(): ',time.time()) #return curent seconds since epoch
print("*********************\n")

print('time.ctime(time.time()): ', time.ctime(time.time())) #return curent time
print("*********************\n")

time_object = time.localtime()
print('time_object: ', time_object)
print("*********************\n")

local_time = time.strftime('%B %d %Y %H:%M:%S ', time_object)
print('local_time: ', local_time)
print("*********************\n")

UTC_time = time.gmtime()
print('UTC_time: ', UTC_time)
print("*********************\n")

time_string = '20 April, 2022'
time_object_1 = time.strptime(time_string, '%d %B, %Y')
print('time_object_1: ', time_object_1)
print("*********************\n")

# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2022, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print('time_string: ', time_string)
print("*********************\n")

time_tuple = (2022, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print('time_string: ', time_string)
print("*********************\n")