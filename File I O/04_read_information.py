with open("information.csv") as file:
    #for line in file:
      #print(line.rstrip("\n"))
        #l = line.rstrip().split(",") it will return a list like this
    for line in file:
        name, city, age = line.rstrip().split(",")
        print(f"My name is {name}, I live in {city} and I am {age} years old")








"""
l =  ['Ali', 'Tehran'] ['Ahmad', 'Yazd'] ['Reza', 'Shiraz'] ['Mohammad', 'Mashhad'] ['Hossein', 'Isfahan'] 

"""
    
    
        

      