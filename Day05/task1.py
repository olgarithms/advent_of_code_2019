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

def task1():
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
            numbers[get_address(mode[2], i, 1, numbers)] = 1
            i += 2
        elif opcode == "04":
            out = numbers[get_address(mode[2], i, 1, numbers)]
            outputs.append(out)
            i += 2
        elif opcode == "99":
            break
        else:
            break
    return outputs[-1]

print(task1())
