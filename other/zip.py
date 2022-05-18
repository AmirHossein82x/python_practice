usernames = ['Dude', 'Bro', 'Mister']
passwords = ['p@ssword', 'abc123', 'guest']
loging_date = [2002, 2003, 2022]

users = dict(zip(usernames, passwords))
print('type: %s' %type(users))

for key, value in users.items():
    print(key + ': ' + value)


print('***********************************\n')


usernames = ['Dude', 'Bro', 'Mister']
passwords = ['p@ssword', 'abc123', 'guest']
loging_date = [2002, 2003, 2022]

user = zip(usernames, passwords, loging_date) #it just show numbers which show where user saved
print(user)

for i in user:
    print(i)

