from math import floor

filename = "input.txt"
fuel = 0

with open(filename, 'r') as textfile:
    for line in textfile:
        mass = int(line)
        fuel += floor(mass / 3) - 2
print(fuel)
