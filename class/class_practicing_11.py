from datetime import datetime, timedelta

class Student:
    def __init__(self, student_name, student_birthday, student_gender):
        self.name = student_name
        self.birthday = student_birthday
        self.gender = student_gender
        self.scores = []



    @property  # if we use this we should use age function without ()
    def age(self):
        year_month_day = list(map(int, self.birthday.split('-')))
        return (datetime.now() - datetime(
               year=year_month_day[0],
               month=year_month_day[1],
               day=year_month_day[2]
                                         )                   
                ).days // 365 



student1 = Student('ali', "2003-1-15", 'male')
student2 = Student('reza', '2015-5-6', 'male')


print(f'student1 is {student1.age} years old')
print(f'student2 is {student2.age} years old')
