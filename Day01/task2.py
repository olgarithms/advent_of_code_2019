from math import floor

filename = "input.txt"
fuel = 0

with open(filename, 'r') as textfile:
    for line in textfile:
        mass = int(line)
        while mass > 0:
            mass = floor(mass / 3) - 2
            if mass > 0:
                fuel += mass
print(fuel)
