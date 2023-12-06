import re
from math import ceil, sqrt

def get_number_of_possible_tries(time, distance):
    # (time - min_time) * min_time > distance
    # Find zeroes of (time - min_time) * min_time - distance
    # = - min_time ** 2 + time * min_time - distance
    # We'll find the first integer greater than the smallest one 
    sqrt_delta = sqrt(time**2 - 4 * distance)
    min_time = (time - sqrt_delta) / 2
    max_time = (time + sqrt_delta) / 2
    ceil_min_time = ceil(min_time)
    floor_max_time = int(max_time)
    min_time = ceil_min_time + 1 if min_time == ceil_min_time else ceil_min_time
    max_time = floor_max_time - 1 if max_time == floor_max_time else floor_max_time
    return max_time - min_time + 1

def part1(times, distances):
    prod = 1
    for time, distance in zip(times, distances):
        prod *= get_number_of_possible_tries(int(time), int(distance))
    return prod
    
def part2(times, distances):
    time = int("".join(times))
    distance = int("".join(distances))
    return get_number_of_possible_tries(time, distance)

with open("input.txt", "r") as f:
    lines = f.readlines()
    times = re.findall("\d+", lines[0])
    distances = re.findall("\d+", lines[1])
    print(part1(times, distances))
    print(part2(times, distances))