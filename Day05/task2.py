filename = "input.txt"
result = None

def get_numbers():
    with open(filename, 'r') as textfile:
        line = textfile.readline().strip("\n")
        return list(map(int, line.split(',')))

def get_parameter(mode, i, pos, numbers):
    return numbers[get_address(mode, i, pos, numbers)]

def get_address(mode, i, pos, numbers):
    # print("mode", mode, "i", i, "pos", pos)
    address = 0
    if mode == "1":
        address = i+pos
    elif mode == "0":
        address = numbers[i+pos]
    return address

def do_arithmetic_operation(addition, multiplication, mode, i, numbers):
    # mode is a 3 digit string that gives modes for each parameter
    param1 = get_parameter(mode[2], i, 1, numbers)
    param2 = get_parameter(mode[1], i, 2, numbers)
    if addition:
        result = param1 + param2
    elif multiplication:
        result = param1 * param2
    numbers[get_address(mode[0], i, 3, numbers)] = result

def do_jump(is_zero, mode, i, numbers):
    param1 = get_parameter(mode[2], i, 1, numbers)
    if ((param1 == 0) and is_zero) or ((param1 != 0) and not is_zero):
        i = get_parameter(mode[1], i, 2, numbers)
    else:
        i += 3
    return i

def do_comparisons(less_than, equals, mode, i, numbers):
    param1 = get_parameter(mode[2], i, 1, numbers)
    param2 = get_parameter(mode[1], i, 2, numbers)
    param3 = get_address(mode[0], i, 3, numbers)
    if (less_than and param1 < param2) or (equals and param1 == param2):
        numbers[param3] = 1
    else:
        numbers[param3] = 0
    return i + 4

def task2():
    numbers = get_numbers()
    i = 0
    outputs = []
    while i < len(numbers) - 1:
        num_str = str(numbers[i])
        zeros_to_add = 5-len(num_str)
        instruction = zeros_to_add*"0" + num_str
        opcode = instruction[-2:]
        mode = instruction[:-2]

        if opcode == "01":
            do_arithmetic_operation(True, False, mode, i, numbers)
            i += 4
        elif opcode == "02":
            do_arithmetic_operation(False, True, mode, i, numbers)
            i += 4
        elif opcode == "03":
            numbers[get_address(mode[2], i, 1, numbers)] = 5
            i += 2
        elif opcode == "04":
            out = numbers[get_address(mode[2], i, 1, numbers)]
            outputs.append(out)
            i += 2
        elif opcode == "05":
            i = do_jump(False, mode, i, numbers)
        elif opcode == "06":
            i = do_jump(True, mode, i, numbers)
        elif opcode == "07":
            i = do_comparisons(True, False, mode, i, numbers)
        elif opcode == "08":
            i = do_comparisons(False, True, mode, i, numbers)
        elif opcode == "99":
            break
        else:
            break
    return outputs[-1]

print(task2())
