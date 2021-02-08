#lists are mutable meaning can be updated changed

my_list = [15,6,3,35,23,12,10,9]
my_strings_list = ['comp sci', 'physics', 'ele engr', 'philly']

print(f'Ints : {my_list}')

print(f'Strings : {my_strings_list}')

print("Sorting...")
my_list.sort()
print(sorted(my_list))

print(f'Sorted ints : {my_list}')

print(f'min value in the list is : {min(my_list)} ')

print('Add/remove.....')

my_list.append(25)
print(my_list)

my_list.insert(4,26)
print(my_list)

my_new_list = ['art', 'econ']

my_strings_list.append(my_new_list)  #appends the new list with the brackets with them so we should not use this
print(my_strings_list)

my_strings_list.extend(my_new_list)
print(my_strings_list)

#pop() vs remove

my_strings_list.remove(my_new_list)
print(my_strings_list)

my_strings_list.pop()  # removes the last index
print(my_strings_list)

#working with sublists
my_list[-1] = 1000
print(my_list)


