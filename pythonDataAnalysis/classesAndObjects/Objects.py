


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

    def find_in_file(self,filename):
        with open(filename) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip())
                student_read_in = Student(first_name, last_name,course_details)
                if self == student_read_in:
                    return True
                else:
                    return False

    def add_to_file(self, filename):
        if self.find_in_file(filename):
            return "Record already exists"
        else:
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(filename,"a+") as to_write:    #"w" will write to a new file and delete the prior entires
                to_write.write(record_to_add+"\n")
            return "Record Added Succesfully"
    @staticmethod
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name+','+ last_name
        courses = ','.join(courses)
        return full_name +':'+courses

    def __eq__(self, other):
        self.first_name == other.first_name and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', '{self.courses}')"

    def __str__(self):
        return f"First Name : {self.first_name.capitalize()}\nLast Name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize,self.courses))}"



courses1 = ['python', 'ruby', 'javascript']
courses2 = ['java', 'c' , 'django']
mashsur = Student("mashur", "hosain", courses1)
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
file_name = "data.txt"
mashur = Student('mashur', 'hossain', ["python", "ruby", "javascript"])
print(mashur.find_in_file(file_name))
print(mashur.add_to_file(file_name))

Joe = Student("Joe", "Shumack", ['JAva', 'Hava', 'Mava'])
print(Joe.find_in_file(file_name))
print(Joe.add_to_file(file_name))
