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