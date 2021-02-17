def func_0(start_num):
    start_num += 1
    return func_1(start_num)


def func_1(start_num):
    start_num += 1
    return start_num


start_num = 1

print(f"start_num\t-> {start_num}")
finish_num = func_0(start_num)
print(f"calc'd_num\t -> {finish_num}")
print(f"stat_num\t -> {start_num}")

print("-" * 40)


def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)


def func_1(another_num):
    another_num[0] += 1
    return another_num


start_num = [1]

print(f"start_num\t-> {start_num}")
finish_num = func_0(start_num)
print(f"calc'd_num\t -> {finish_num}")
print(f"stat_num\t -> {start_num}")
