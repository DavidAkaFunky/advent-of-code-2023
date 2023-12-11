def get_valid_neighbours(i, j, tile, max_i, max_j):
    neighbours = []
    if i > 0 and tile in "|LJS" and lines[i-1][j] in "|7FS":
        neighbours.append([i-1, j])
    if i < max_i and tile in "|7FS" and lines[i+1][j] in "|LJS":
        neighbours.append([i+1, j])
    if j > 0 and tile in "-J7S" and lines[i][j-1] in "-LFS":
        neighbours.append([i, j-1])
    if j < max_j and tile in "-LFS" and lines[i][j+1] in "-J7S":
        neighbours.append([i, j+1])
    return neighbours    
    
def transform_start(lines, path):
    start_i, start_j = path[0]
    second_i, second_j = path[1]
    last_i, last_j = path[-1]
    diff = (last_i - second_i, last_j - second_j)
    matches = {(0, -1): "-", (0, 1): "-",
               (1, 0): "|", (-1, 0): "|",
               (-1, 1): "F", (-1, -1): "7",
               (1, 1): "L", (1, -1): "J"}
    lines[start_i][start_j] = matches[diff]
    
def part1(lines):
    max_i, max_j = len(lines) - 1, len(lines[0]) - 1
    for i in range(max_i):
        for j in range(max_j):
            if lines[i][j] == "S":
                path = [[i, j, "S", []]]
    while True:
        i, j, tile, p = path.pop(0)
        if tile == "S" and len(p) > 0:
            return len(p) // 2, p
        for n in get_valid_neighbours(i, j, tile, max_i, max_j):
            if len(p) == 0 or n != p[-1]:
                path.append(n + [lines[n[0]][n[1]], p + [[i, j]]])

def part2(lines, path):
    count = 0
    leave_at = None
    for i, line in enumerate(lines):
        inside = False
        for j, tile in enumerate(line):
            if (i, j) in path:
                match tile:
                    case "F":
                        leave_at = "7"
                    case "L":
                        leave_at = "J"
                    case "-":
                        continue
                    case _:
                        if tile != leave_at:
                            inside = not inside
                        leave_at = None
            elif inside:
                count += 1
    return count


with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    dist, path = part1(lines)
    print(dist)
    transform_start(lines, path)
    path = {tuple(pos) for pos in path}
    print(part2(lines, path))