from datetime import datetime

# encapsulate
class Student:
    def __init__(self, name, birthday, gender):
        self.name = name
        self.birthday = birthday
        # private - encapsulate
        self.__gender = gender
        self.__scores = [20, 12, 9, 7]

    @property
    def gender(self):
        return self.__gender
    
    @property
    def scores(self):
        for index, item in enumerate(self.__scores):
            if item < 10:
                self.__scores[index] = 0
        return self.__scores

    @scores.setter
    def scores(self, scores):
        for score in scores:
            if 0 <= score <= 20:
                self.__scores.append(score)
            else:
                print('Invalid score')

    @scores.deleter
    def scores(self):
        self.__scores.clear()

    @property
    def age(self):
        year,month, day =list(map(int, self.birthday.split('-'))) 
        age =  (datetime.utcnow() - datetime(year=year, month=month, day=day)).days // 365
        return 'You are %d years old' %age





ali = Student('ali', "2003-04-15", 'male')
print(ali.name)
print(ali.birthday)
#print(ali.__gender)    # Error:  Student' object has no attribute '__gender'

print(ali.scores)    # [20, 12, 0, 0]

ali.scores = [11, 23, 6]  

print(ali.scores)    # [20, 12, 0, 0, 11, 0]

print(ali.age)

print(ali.gender)