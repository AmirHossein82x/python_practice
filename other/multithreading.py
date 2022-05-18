import threading
import time

#print(threading.active_count())
#print(threading.enumerate())

def eat_breakfast():
    time.sleep(5)
    print('you eat breakfast')

def drink_coffee():
    time.sleep(2)
    print('you drink coffee')

def study():
    time.sleep(6)
    print('you finish studing')

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join() # if I don't use this function threading.active_count will show 4 but if I use this 
z.join() # ... function threading.active_count will show 1


"""
if i did not use x, y, z : program will start normally 
which means at first eat_breakfast perform and then drink_coffee and then study perform
but when I use x, y, z the the functions perform at the same time
which means the whole program takes 5 seconds to complete
in this situation order doesn't matter, time is just matterd and which function has fewer seconds it will perform first 

"""

#eat_breakfast()
#drink_coffee()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())