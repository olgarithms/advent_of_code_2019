def read_input():
    with open("input.txt", "r") as textfile:
        directions1 = textfile.readline().strip("\n").split(",")
        directions2 = textfile.readline().strip("\n").split(",")
    return (directions1, directions2)

def make_path(directions):
    dir_x = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    dir_y = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
    path = set()
    (x, y) = (0, 0)
    steps = 0
    steps_to_points = {}
    for i in directions:
        direction = i[0]
        n = int(i[1:])
        for _ in range(n):
            x += dir_x[direction]
            y += dir_y[direction]
            path.add((x, y))
            steps += 1
            if (x,y) not in steps_to_points:
                steps_to_points[(x,y)] = steps
    return path, steps_to_points

def find_common_points(path1, path2):
    return set(path1) & set(path2)

def find_closest_intersection(common_points):
    return min([abs(x) + abs(y) for (x,y) in common_points])

def find_fewer_steps(common_points, steps_to_points1, steps_to_points2):
    return min(steps_to_points1[point] + steps_to_points2[point] for point in common_points)

(directions1, directions2) = read_input()
(path1, steps_to_points1) = make_path(directions1)
(path2, steps_to_points2) = make_path(directions2)
common_points = find_common_points(path1, path2)

task1 = find_closest_intersection(common_points)
print(task1)

task2 = find_fewer_steps(common_points, steps_to_points1, steps_to_points2)
print(task2)
