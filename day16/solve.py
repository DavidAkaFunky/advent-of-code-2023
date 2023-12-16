from queue import Queue

def get_value(lines, pos):
    return lines[pos[0]][pos[1]]

def get_new_pos(pos, _dir):
    match _dir:
        case "N":
            return (pos[0] - 1, pos[1])
        case "S":
            return (pos[0] + 1, pos[1])
        case "E":
            return (pos[0], pos[1] + 1)
        case "W":
            return (pos[0], pos[1] - 1)
        
def get_mirrored_dir(_dir, mirror):
    match _dir:
        case "N":
            return "E" if mirror == "/" else "W"
        case "S":
            return "W" if mirror == "/" else "E"
        case "E":
            return "N" if mirror == "/" else "S"
        case "W":
            return "S" if mirror == "/" else "N"
        
def get_split_dirs(_dir, split):
    if _dir in "NS" and split == "-":
        return ["E", "W"]
    if _dir in "EW" and split == "|":
        return ["N", "S"]
    return _dir

def part1(lines, start=(0, 0), start_dir="E"):
    max_i = len(lines) - 1
    max_j = len(lines[0]) - 1
    visited = set()
    q = Queue()
    q.put(start + (start_dir,))
    while not q.empty():
        node = q.get()
        if node in visited:
            continue
        visited.add(node)
        pos, _dir = node[:-1], node[-1]
        value = get_value(lines, pos)
        match value:
            case "/" | "\\":
                _dir = get_mirrored_dir(_dir, value)
            case "-" | "|":
                _dir = get_split_dirs(_dir, value)
        _dir = list(_dir)
        for d in _dir:
            new_pos = get_new_pos(pos, d)
            if 0 <= new_pos[0] <= max_i and 0 <= new_pos[1] <= max_j:
                q.put(new_pos + (d,))
    return len(set(pos[:-1] for pos in visited))

def part2(lines):
    _max = max(part1(lines, start=(len(lines) - 1, i), start_dir="N") for i in range(len(lines[0])))
    _max = max([part1(lines, start=(0, i), start_dir="S") for i in range(len(lines[0]))] + [_max])
    _max = max([part1(lines, start=(i, 0), start_dir="E") for i in range(len(lines[0]))] + [_max])
    _max = max([part1(lines, start=(i, len(lines[0]) - 1), start_dir="W") for i in range(len(lines[0]))] + [_max])
    return _max

with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    print(part1(lines))
    print(part2(lines))