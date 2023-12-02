import re
from functools import reduce

colour_list = ["red", "green", "blue"]

def get_colour_values(set):
    return [re.findall(f"\d+ {colour}", set) for colour in colour_list]

def part1(lines):
    sum = 0
    limits = [12, 13, 14]
    for line in lines:
        id, games = line.split(":")
        id = int(id.split()[1])
        games = games.split(";")
        valid = True
        for set in games:
            colours = get_colour_values(set)
            for colour, limit in zip(colours, limits):
                try:
                    colour = int(colour[0].split()[0])
                    if colour > limit:
                        valid = False
                        break
                except:
                    continue
            if not valid:
                break
        if valid:
            sum += id
    return sum
            

def part2(lines):
    sum = 0
    for line in lines:
        games = line.split(":")[1].split(";")
        limits = [0, 0, 0]
        for set in games:
            colours = get_colour_values(set)
            for i in range(len(limits)):
                try:
                    colour = int(colours[i][0].split()[0])
                    limits[i] = max(limits[i], colour)
                except:
                    continue
        sum += reduce(lambda x, y: x * y, limits)
    return sum


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines)) # 1734
    print(part2(lines)) # 70387