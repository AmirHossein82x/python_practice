print("hello {name} I am here for you to play {sport}".format(name="ali", sport="football"))
#print("hello {1} I am here for you to play {0}".format(name="ali", sport="football")) error
#print(name)    error
a = "hossein"
b = "hi"
print("{1} {0} how are you".format(a, b))
print("{} {} how are you".format(a, b))
print("{} {:10} how are you".format(a, b))
print("{} {:>10} how are you".format(a, b))
print("{} {:^5} how are you".format(a, b))
number = 3.14567
print("The number is {:.2f}".format(number))
number2 = 10007878
print("The number is {:,}".format(number2))