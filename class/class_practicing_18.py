class Student:
    """
    we can understand how many Student we generate in the whole program
    
    """
    count = 0
    student_list = []

    def __init__(self, name, score):

        self.__name = name
        self.__score = score
        Student.count += 1
        Student.student_list.append(self)

    def __str__(self):
        return "%s" %self.__name

a = Student('ali', 20)
a = Student('reza', 12)
a = Student('hsssan', 18)
print(Student.count)
for item in Student.student_list:
    print(item)