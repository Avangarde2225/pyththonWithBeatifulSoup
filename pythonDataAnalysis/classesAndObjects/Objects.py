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

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', '{self.courses}')"

    def __str__(self):
        return f"First Name : {self.first_name.capitalize()}\nLast Name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize,self.courses))}"



courses1 = ['python', 'rails', 'java']
courses2 = ['java', 'c' , 'django']
mashsur = Student("mashur", "husain", courses1)
john = Student('john', 'Doe', courses2)

# print(mashsur.first_name, mashsur.last_name, mashsur.courses)
# print(john.first_name, john.last_name, john.courses)

# mashsur.add_course('java')
# print(mashsur.courses)
# mashsur.add_course('c#')
# print(mashsur.courses)
#
# john.remove_course("c")
# john.remove_course("c")
# john.remove_course("python")
# print(john.courses)

print("-" * 40)
print(mashsur)
print(john)
# print(len(mashsur))
# print(repr(mashsur))

