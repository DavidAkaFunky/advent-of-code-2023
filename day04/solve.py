import re
from functools import reduce

def get_number_of_intersections(line):
    winners, numbers = [set(re.findall("\d+", part)) for part in line.split(":")[1].split("|")]
    return len(winners.intersection(numbers))

def part1(intersections):
    return reduce(lambda x, y: x + y, 
                  map(lambda v: 2 ** (v[0] - 1), 
                      filter(lambda v: v[0] != 0, intersections.values())))
    
def part2(intersections):
    sum = 0
    for k in intersections:
        matches, times = intersections[k]
        sum += times
        for i in range(1, matches + 1):
            intersections[k + i][1] += times
    return sum

with open("input.txt", "r") as f:
    lines = f.readlines()
    intersections = {i: [get_number_of_intersections(lines[i]), 1] for i in range(len(lines))}
    print(part1(intersections)) # 26346
    print(part2(intersections)) # 8467762