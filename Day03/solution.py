def read_input():
    with open("input.txt", "r") as textfile:
        directions1 = textfile.readline().strip("\n").split(",")
        directions2 = textfile.readline().strip("\n").split(",")
    return (directions1, directions2)

def make_path(directions):
    path = set()
    (x, y) = (0, 0)
    for i in directions:
        if i[0] == "U":
            for j in range(int(i[1:])):
                y += 1
                path.add((x, y))
        elif i[0] == "L":
            for j in range(int(i[1:])):
                x -= 1
                path.add((x, y))
        elif i[0] == "R":
            for j in range(int(i[1:])):
                x += 1
                path.add((x, y))
        elif i[0] == "D":
            for j in range(int(i[1:])):
                y -= 1
                path.add((x, y))
        else:
            break
    return path

def find_common_points(path1, path2):
    return set(path1) & set(path2)

def find_closest_intersection(common_points):
    return min([abs(x)+abs(y) for (x,y) in common_points])

(directions1, directions2) = read_input()
path1 = make_path(directions1)
path2 = make_path(directions2)
common_points = find_common_points(path1, path2)

task1 = find_closest_intersection(common_points)
print(task1)
