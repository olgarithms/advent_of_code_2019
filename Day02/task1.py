filename = "input.txt"
result = None

# Read the input
with open(filename, 'r') as textfile:
    line = textfile.readline().strip("\n")
    numbers = [int(x) for x in line.split(",")]

# Go to state "1202 program alarm"
numbers[1] = 12
numbers[2] = 2

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

result = numbers[0]
print(numbers)
print(result)
