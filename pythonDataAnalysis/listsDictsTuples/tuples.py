my_random_tuple = ('first', 'second', 1,2,3,4,5,6,7,'hi there', 10,11,12,14)

my_tuple = ('sirt_value', 'second_value', 'third_value')

print(my_random_tuple[0])
print(my_random_tuple[-1])
print(my_random_tuple[::-1]) #reverse order

print(len(my_random_tuple))
print(my_random_tuple.count(5))
print(my_random_tuple.index(5))

first_var, second_var, third_var = my_tuple
print(first_var)

two_tuples= my_tuple + my_random_tuple
print(two_tuples)
print(len(two_tuples))
