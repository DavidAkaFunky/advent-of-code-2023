from collections import Counter
from copy import deepcopy

def get_load(lines):
    _sum = 0
    for i, line in enumerate(lines):
        counts = Counter(line)
        _sum += counts["O"] * (len(lines) - i)
    return _sum

def tilt_north(lines):
    for j in range(len(lines[0])):
        for i in range(1, len(lines)):
            if lines[i][j] != "O":
                continue
            k = i
            while k > 0 and lines[k-1][j] == ".":
                lines[k][j], lines[k-1][j] = lines[k-1][j], lines[k][j]
                k -= 1
    
def tilt_south(lines):
    for j in range(len(lines[0])):
        for i in range(len(lines) - 1, -1, -1):
            if lines[i][j] != "O":
                continue
            k = i
            while k < len(lines) - 1 and lines[k+1][j] == ".":
                lines[k][j], lines[k+1][j] = lines[k+1][j], lines[k][j]
                k += 1
                
def tilt_east(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 1, -1, -1):
            if lines[i][j] != "O":
                continue
            k = j
            while k < len(lines[0]) - 1 and lines[i][k+1] == ".":
                lines[i][k], lines[i][k+1] = lines[i][k+1], lines[i][k]
                k += 1
    
def tilt_west(lines):
    for i in range(len(lines)):
        for j in range(1, len(lines[0])):
            if lines[i][j] != "O":
                continue
            k = j
            while k > 0 and lines[i][k-1] == ".":
                lines[i][k], lines[i][k-1] = lines[i][k-1], lines[i][k]
                k -= 1
    
    
def tilt(lines, orientation):
    new_lines = deepcopy(lines)
    match orientation:
        case "N":
            tilt_north(new_lines)
        case "S":
            tilt_south(new_lines)
        case "E":
            tilt_east(new_lines)
        case "W":
            tilt_west(new_lines)
    return new_lines
            
def part1(lines):
    return get_load(tilt(lines, "N"))

def part2(lines):
    orientations = "NWSE"
    states = [lines]
    state = lines
    while True:
        for o in orientations:
            state = tilt(state, o)
        try:
            first_in_loop = states.index(state)
            period = len(states) - first_in_loop
            final = states[first_in_loop + (1000000000 - first_in_loop) % period]
            return get_load(final)
        except ValueError:
            states.append(state)

with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    print(part1(lines))
    print(part2(lines))