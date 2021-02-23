class Student:

    def __init__(self,first_name, last_name, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        if courses ==None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled the {course} course")

    def remove_course(self,course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} is not found")

courses1 = ['python', 'rails', 'java']
courses2 = ['java', 'c' , 'django']
mashsur = Student("mashur", "husain", courses1)
john = Student('john', 'Doe', courses2)

print(mashsur.first_name, mashsur.last_name, mashsur.courses)
print(john.first_name, john.last_name, john.courses)

mashsur.add_course('java')
print(mashsur.courses)
mashsur.add_course('c#')
print(mashsur.courses)

john.remove_course("c")
john.remove_course("c")
john.remove_course("python")
print(john.courses)