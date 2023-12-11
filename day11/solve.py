import re
from functools import reduce

def dist(p1, p2, lines_no_galaxies, columns_no_galaxies, expansion):
    p1_i, p1_j = p1
    p2_i, p2_j = p2
    if p1_i > p2_i:
        p1_i, p2_i = p2_i, p1_i
    if p1_j > p2_j:
        p1_j, p2_j = p2_j, p1_j
    dist = 0
    for i in range(p1_i + 1, p2_i + 1):
        dist += expansion if i in lines_no_galaxies else 1
    for j in range(p1_j + 1, p2_j + 1):
        dist += expansion if j in columns_no_galaxies else 1
    return dist

def solve(matrix, expansion):
    galaxies = [(i, m.start(0)) for i, line in enumerate(matrix) for m in re.finditer("#", "".join(line))]
    lines_no_galaxies = set(range(len(matrix))) - set(map(lambda x: x[0], galaxies))
    columns_no_galaxies = set(range(len(matrix))) - set(map(lambda x: x[1], galaxies))
    return reduce(lambda x, y: x + y, [dist(galaxies[i], galaxies[j], lines_no_galaxies, columns_no_galaxies, expansion) 
                                       for i in range(len(galaxies) - 1) 
                                       for j in range(i+1, len(galaxies))])
        
with open("input.txt", "r") as f:
    matrix = [line.strip() for line in f.readlines()]
    print(solve(matrix, 2))
    print(solve(matrix, 10**6))