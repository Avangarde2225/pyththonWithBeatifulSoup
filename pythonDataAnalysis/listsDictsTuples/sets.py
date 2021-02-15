#sets dont have orders so index cannot be used
#you cannot have duplicates in sets

my_set={1,2,3,'java', 'ruby', 8,9,20,2000, 20}
my_list = [15,6,3,35,23,12,10,15,'java',9, 35,35,6,'java']

print('java' in my_set) # returns  boolean
print(my_list)

my_set = set(my_list)

print(my_set)
