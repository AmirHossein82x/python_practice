friends = [('rachle', 19), 
           ('monica', 18), 
           ('phoebe', 17), 
           ('joey', 16), 
           ('chandler', 21), 
           ('ross', 20)]
    
age = lambda age: age[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i[0].capitalize() + ":" + str(i[1]))