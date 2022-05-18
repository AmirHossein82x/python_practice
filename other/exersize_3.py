result = 0
a = []
for number in range(2, 1001):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        result += number
        a.append(number)
print(a)
print(result)
