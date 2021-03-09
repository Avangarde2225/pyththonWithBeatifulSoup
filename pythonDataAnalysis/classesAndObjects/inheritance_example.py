class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses


class StudentAtlethe(Student):
    pass

courses = ['python', 'java', 'hava']
jane = StudentAtlethe('jane','doe',courses)
print(jane.courses)
