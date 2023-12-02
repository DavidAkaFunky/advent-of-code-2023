import re

def part1(lines):
    sum = 0
    
    for line in lines:
        matches = re.findall("\d", line)
        if len(matches) == 0:
            continue
        sum += int(matches[0]) * 10 + int(matches[-1])
        
    return sum


def part2(lines):
    replacements = {"one": 1, "two": 2, "three": 3,
                    "four": 4, "five": 5, "six": 6,
                    "seven": 7, "eight": 8, "nine": 9}
    
    def parse_int(number):
        try:
            return int(number)
        except ValueError:
            return replacements[number]
    
    number_regex = f"(?=(\d|{'|'.join(replacements.keys())}))"
    sum = 0
    
    for line in lines:
        matches = re.findall(number_regex, line)
        sum += parse_int(matches[0]) * 10 + parse_int(matches[-1])
        
    return sum


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines)) # 55477
    print(part2(lines)) # 54431