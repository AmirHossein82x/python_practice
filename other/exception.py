try:
    numerator = int(input("enter a number to divide: "))
    denumerator = int(input("enter a number to divide by: "))
    result = numerator / denumerator
except ZeroDivisionError as e:
    print(e)
    print("you can't divide number to zero! ")
except ValueError as e:
    print(e)
    print("just use number ")
except Exception as e:    # mahz ehtiat az exception estefadeh mikon7im
    print(e)
    print("some thing went wrong")
else:
    print(result)
finally:
    print('This will always be shown')

