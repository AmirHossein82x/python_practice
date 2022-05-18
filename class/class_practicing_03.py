class point:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def greeting(self):
        print("hello %s\nyour last name is %s\nwelcome to this program" %(self.first_name, self.last_name))
a = point("amir hossein", "ghasemi")
a.greeting()