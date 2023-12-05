import re
from copy import deepcopy
    
def part1(seeds, mappings):
    min_value = 2 ** 64
    for seed in seeds:
        for mapping in mappings:
            for map_range in mapping:
                diff = seed - map_range[1]
                if 0 <= diff < map_range[2]:
                    seed = map_range[0] + diff
                    break
        min_value = min(min_value, seed)
    return min_value
    
def part2(seeds, mappings):
    min_value = 2 ** 64
    for i in range(0, len(seeds) - 1, 2):
        seed_ranges = [(seeds[i], seeds[i] + seeds[i+1])]
        for mapping in mappings:
            seed_ranges = {seed_range: False for seed_range in seed_ranges}
            for map_range in mapping:
                map_min, map_max = map_range[1], map_range[1] + map_range[2]
                diff = map_range[0] - map_min
                for seed_range in deepcopy(seed_ranges):
                    if seed_ranges[seed_range] or seed_range[1] <= map_min or map_max <= seed_range[0]:
                        continue
                    seed_ranges.pop(seed_range)
                    if seed_range[0] < map_min:
                        seed_ranges[(seed_range[0], map_min)] = False
                        seed_range = (map_min, seed_range[1])
                    if map_max < seed_range[1]:
                        seed_ranges[(map_max, seed_range[1])] = False
                        seed_range = (seed_range[0], map_max)
                    seed_ranges[(seed_range[0] + diff, seed_range[1] + diff)] = True
        min_value = min(min_value, min(map(lambda x: x[0], seed_ranges)))            
    return min_value

with open("input.txt", "r") as f:
    parts = f.read().split("\n\n")
    seeds, mappings = parts[0], parts[1:]
    seeds = [int(value) for value in re.findall("\d+", seeds)]
    mappings = [[[int(value) for value in line.split()] for line in part.split("\n")[1:]] for part in mappings]
    print(part1(seeds, mappings))
    print(part2(seeds, mappings))