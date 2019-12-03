filename = "input.txt"
result = None

def get_numbers():
    with open(filename, 'r') as textfile:
        line = textfile.readline().strip("\n")
        return list(map(int, line.split(',')))

def task1(noun, verb):
    numbers = get_numbers()
    numbers[1] = noun
    numbers[2] = verb
    # Run the program
    i = 0
    while i < len(numbers) - 1:
        if numbers[i] == 1: # do addition
            numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
            i += 4
        elif numbers[i] == 2: # do multiplication
            numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]
            i += 4
        elif numbers[i] == 99:
            break
        else:
            break
    return numbers[0]

for x in range(100):
    for y in range(100):
        if task1(x, y) == 19690720:
            result = 100 * x + y
            break
print(result)
