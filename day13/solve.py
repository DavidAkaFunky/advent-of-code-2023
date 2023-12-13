def transpose_matrix(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

def is_mirror(pattern, i, j, fix_smudge):
    x = 0
    while i-x >= 0 and j+x < len(pattern):
        diff = [pattern[i-x][k] != pattern[j+x][k] for k in range(len(pattern[i-x]))]
        if fix_smudge and sum(diff) == 1:
            fix_smudge = False
            x += 1
            continue
        if sum(diff) != 0:
            return 0
        x += 1
    return i+1

def get_mirror(pattern, fix_smudge, old_reflection=""):
    for i in range(len(pattern)-1):
        if f"r{i}" == old_reflection:
            continue # Skip reflections found in part 1
        value = is_mirror(pattern, i, i+1, fix_smudge)
        if value > 0:
            return value * 100, f"r{i}"
    pattern = transpose_matrix(pattern)
    for i in range(len(pattern)-1):
        if f"c{i}" == old_reflection:
            continue # Skip reflections found in part 1
        value = is_mirror(pattern, i, i+1, fix_smudge)
        if value > 0:
            return value, f"c{i}"
    return 0, ""

def part1(patterns):
    _sum = 0
    reflections = []
    for pattern in patterns:
        value, reflection = get_mirror(pattern, False)
        _sum += value
        reflections.append(reflection)
    return _sum, reflections

def part2(patterns, old_reflections):
    _sum = 0
    for i, pattern in enumerate(patterns):
        value, _ = get_mirror(pattern, True, old_reflection=old_reflections[i])
        _sum += value
    return _sum

with open("input.txt") as f:
    patterns = [[list(line) for line in pattern.split("\n")] for pattern in f.read().split("\n\n")]
    _sum, old_reflections = part1(patterns)
    print(_sum)
    print(part2(patterns, old_reflections)) 