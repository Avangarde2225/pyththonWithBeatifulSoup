i=0
while i < 10:
    print(i)
    i +=1

print('-' * 40)

from random import randint
l1 = [randint(1,100) for num in range (1000)]
i=0
num_to_search = 25
while i< len(l1):
    if l1[i] == num_to_search:
        print(f"{num_to_search} found at index {i}")
        break
    i += 1

print('-' * 40)

l2 = [".py", ".js", ".rb", ".java", ".c"]
l3 = ["python", " javascript", "ruby", "java" , "c"]

tupled_list = list(zip(l3,l2))
print(tupled_list)

