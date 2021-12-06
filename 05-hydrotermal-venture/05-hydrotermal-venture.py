def perpendicular(paths):
    return [((x0,y0),(x1,y1)) for ((x0,y0),(x1,y1)) in paths if x0 == x1 or y0 == y1]

def diagonal(paths):
    return [((x0,y0),(x1,y1)) for ((x0,y0),(x1,y1)) in paths if x0 != x1 and y0 != y1]

def my_zip(l1, l2):
    return [(l1[i], l2[i]) for i in range(len(l1))]

def to_mark(point):
    match point:
        case ((x0,y0),(x1,y1)) if x0 == x1:
            return [(x0, y) for y in (range(y0, y1 + 1) if y1 > y0 else range(y1, y0 + 1))]
        case ((x0,y0),(x1,y1)) if y0 == y1:
            return [(x, y0) for x in (range(x0, x1 + 1) if x1 > x0 else range(x1, x0 + 1))]
        case ((x0,y0),(x1,y1)):
            return my_zip(
                range(x0, x1 + 1) if x1 > x0 else range(x0, x1 - 1, -1),
                range(y0, y1 + 1) if y1 > y0 else range(y0, y1 - 1, -1))

def dangerous_spots(grid):
    return sum([1 if grid[i][j] >= 2 else 0
        for i in range(len(grid))
        for j in range(len(grid))])

file = open('05-hydrotermal-venture-input.txt', 'r')
paths = [(
    tuple([int(x) for x in a.split(",")]),
    tuple([int(x) for x in b.split(",")]),
) for (a,b) in [tuple(p.strip().split(" -> ")) for p in file.readlines()]]
max_x = max(
    max([a for ((a, _), (_, _)) in paths]),
    max([a for ((_, _), (a, _)) in paths]))
max_y = max(
    max([a for ((_, a), (_, _)) in paths]),
    max([a for ((_, _), (_, a)) in paths]))
grid = [[0] * (max_x + 1) for _ in range(max_y + 1)]

for (x,y) in [m for p in perpendicular(paths) for m in to_mark(p)]:
    grid[x][y] += 1
print(dangerous_spots(grid))

for (x,y) in [m for p in diagonal(paths) for m in to_mark(p)]:
    grid[x][y] += 1
print(dangerous_spots(grid))