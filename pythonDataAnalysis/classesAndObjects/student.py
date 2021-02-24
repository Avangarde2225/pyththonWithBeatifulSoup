

file_name = "data.txt"
# f = open(file_name)
# # f_content = f.readline()  #reads only the firstline of the file
# # f_content = f.read()   #reads all the lines
#
# for line in f:
#     print(line.strip())
# f.close()
def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(",")
    course_details = line[1].rstrip().split(",")
    return first_name, last_name, course_details

def prep_to_write(first_name, last_name, courses):
    full_name = first_name+','+last_name
    courses = ",".join(courses)
    return full_name+':'+courses

#to read the file using with
with open(file_name) as f:
    for line in f:
        print(line.strip())
        first_name, last_name, course_details = prep_record(line)
        print(first_name,last_name,course_details)


record_to_add = "john,schome:python, java, jugo"


# #to write in a file
# record_to_add = "john,schome:python, java, jugo"
# with open(file_name,"a+") as to_write:    #"w" will write to a new file and delete the prior entires
#     to_write.write(record_to_add+"\n")



# mashur = Student('mashur','hosain',['python','ruby','javascript'])
# print(mashur.find_in_file(file_name))
# print(mashur.add_to_file(file_name))