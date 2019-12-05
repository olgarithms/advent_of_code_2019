def check_if_any_same_adjacent(num):
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            return True
    return False

def check_two_same_adjacent(num):
    last_digit = num[0]
    group_len = 1
    for i in num[1:]:
        if i == last_digit:
            group_len += 1
        else:
            if group_len == 2:
                return True
            last_digit = i
            group_len = 1
    return group_len == 2

def check_if_digits_in_order(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

given_range = "147981-691423"
(mini, maxi) = map(int, given_range.split("-"))

task1 = 0
task2 = 0
for num in range(mini, maxi):
    num_str = str(num)
    if check_if_any_same_adjacent(num_str) and check_if_digits_in_order(num_str):
        task1 += 1
        if check_two_same_adjacent(num_str):
            task2 += 1
print(task1, task2)
