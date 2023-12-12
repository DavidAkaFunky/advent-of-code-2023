import functools

@functools.cache
def get_valid_arrangements(line, groups):
    if line == "":
        return len(groups) == 0
    match line[0]:
        case "?":
            # Skip or replace with "#"
            return get_valid_arrangements(line[1:], groups) + \
                   get_valid_arrangements("#" + line[1:], groups)
        case ".":
            return get_valid_arrangements(line[1:], groups)
        case "#":
            if len(groups) == 0:
                # No groups left but "#" left
                return 0
            group = groups[0]
            next_dot = line.find(".")
            if next_dot == -1:
                next_dot = len(line)
            if next_dot < group:
                # Not enough "#" for this group
                return 0
            remainder = line[group:]
            if len(remainder) == 0:
                # Check base case
                return get_valid_arrangements(remainder, groups[1:])
            if remainder[0] == "#":
                # Too many "#" for this group
                return 0
            # We know the next char will be ".", skip it and check next group
            return get_valid_arrangements(remainder[1:], groups[1:])

def solve(lines, part):
    sum = 0
    for line in lines:
        line, groups = line.split()
        groups = [int(x) for x in groups.split(",")]
        if part == 2:
            line = "?".join([line for _ in range(5)])
            groups *= 5
        sum += get_valid_arrangements(line, tuple(groups))
    return sum

with open("input.txt", "r") as f:
    lines = f.readlines()
    print(solve(lines, 1))
    print(solve(lines, 2))