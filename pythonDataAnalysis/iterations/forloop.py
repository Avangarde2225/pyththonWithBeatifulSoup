l = [1,2,3,4,5,5,6,7,7,8,8,9,9]
my_dict = {'py':'python', 'rb':'ruby', 'js':'javascript'}

sum = 0
for num in l:
    sum = sum+num

print(f"sum using list: {sum}")

for num in range(10):
    print(num)
print('*'* 40)

for num in range(len(l)):
    print(l[num])

print("working with the dictionaries")

for item in my_dict:
    print(item)

for key,value in my_dict.items():
    print(f"key is {key}, and value is {value}")

print("*"* 40)

#generate 100 random integers between 1 and 100
from random import randint
l1 = []
for num in range(100):
    l1.append(randint(1,100))
print(l1)

#another way

l1 = [randint(1,100) for num in range(100)]
print(l1)

l2 = [num for num in range(100)]   #orderly way
print(l2)

