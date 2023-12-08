from math import lcm

def end_cond_part1(node):
    return node == "ZZZ"

def end_cond_part2(node):
    return node[-1] == "Z"

def solve(order, mappings, end_cond, node):
    i, steps = 0, 0
    while True:
        steps += 1
        node = mappings[node][order[i]]
        if end_cond(node):
            return steps
        i = (i + 1) % len(order)

def part1(order, mappings):
    return solve(order, mappings, end_cond_part1, "AAA")

def part2(order, mappings):
    return lcm(*[solve(order, mappings, end_cond_part2, node) for node in mappings if node[-1] == "A"])

with open("input.txt", "r") as f:
    lines = f.readlines()
    order = lines[0].strip()
    mappings = {}
    for i, line in enumerate(lines[2:]):
        line = line.split()
        mappings[line[0]] = {"L": line[2][1:-1], "R": line[3][:-1]}
    print(part1(order, mappings))
    print(part2(order, mappings))