class Student:
    def __init__(self, name, scores):
        self.name = name
        self.__scores = scores

    @property
    def scores(self):
        self.__scores = [score for score in self.__scores if 0 <= score <= 20]
        return self.__scores

    @scores.setter
    def scores(self, scores_list):
        self.__scores = [score for score in scores_list if 0 <= score <= 20]

    @property
    def avg(self):
        result = [score for score in self.__scores if 0 <= score <= 20]
        try:
            return (sum(result) // len(result))
        except ZeroDivisionError:
            return f"nothing because {self.name} has no valid score"


information = {}

student_number = int(input('how many students would you like to enter:? '))

for i in range(student_number):
    name, *sco = input('enter name and scores of student: ').split()
    scores = list(map(int, sco))
    information[name] = Student(name, scores)


for key, value in information.items():
    print(f"{key}'s scores are {information[key].scores}")
    print(f"{key}'s avg is {information[key].avg}\n")
    print("**************************************\n")

logic = True
while logic:

    answer = input('would you like to change scores of any student? (yes, no): ').lower()
    if answer == "no":
        print('Good luck')
        logic = False

    elif answer == "yes":

        while True:

            answer2 = input('enter a name of the student that would you want to change his score: ')
            new_score = list(map(int, input('enter new scores: ').split()))
            information[answer2].scores = new_score
            final = input('would you want to change another scores? ').lower()
            if final == 'no':
                break

        while True:

            add_student = input('would you want to add a new student? ').lower()
            if add_student == 'no':
                break

            else:

                new_name = input("what is new student's name: ")
                new_scores = list(map(int, input("enter student's new number: ").split()))
                information[new_name] = Student(name, new_scores)
                another = input('would you like to continue? ').lower()
                if another == "no":
                    break

        new_info = input('would you want to see the latest changes? ').lower()
        if new_info == "no":
            logic = False

        else:
            print("**************************************\n")
            print('new information with the latest changes: \n')
            for key, value in information.items():
                print(f"{key}'s scores are {information[key].scores}")
                print(f"{key}'s avg is {information[key].avg}\n")
                print("**************************************\n")
        print('Good luck')
        logic = False