from functools import reduce

def get_adjacent_positions(pos, max_i, max_j):
    (i, j) = pos
    min_i = max(0, i-1)
    max_i = min(max_i, i+1)
    min_j = max(0, j-1)
    max_j = min(max_j, j+1)
    return [(pos_i, pos_j) for pos_i in range(min_i, max_i+1) for pos_j in range(min_j, max_j+1) if (pos_i, pos_j) != pos]

def process_number(visited_digits, digit):
    if visited_digits[digit]: # To avoid repeated numbers
        return 0
    number = 0
    exp = 0
    (i, j) = digit
    try:
        # Go to the end of the number
        # (stopping at either a symbol or the end of the map)
        while grid[i][j+1].isdigit():
            j += 1
    except:
        pass 
    
    # Reconsruct the number
    while True:
        try:
            number += int(grid[i][j]) * (10 ** exp)
            visited_digits[(i, j)] = True
        except:
            break
        exp += 1
        j -= 1
    return number

def part1(grid):
    symbols = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] not in "0123456789."]
    max_i, max_j = len(grid)-1, len(grid[0])-1
    adj_digits = [(i, j) for symbol in symbols for (i, j) in get_adjacent_positions(symbol, max_i, max_j) if grid[i][j].isdigit()]
    visited_digits = {pos: False for pos in adj_digits}
    sum = 0
    for digit in adj_digits:
        sum += process_number(visited_digits, digit)
    return sum
    
def part2(grid):
    symbols = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "*"]
    max_i, max_j = len(grid)-1, len(grid[0])-1
    sum = 0
    for symbol in symbols:
        adj_digits = [(i, j) for (i, j) in get_adjacent_positions(symbol, max_i, max_j) if grid[i][j].isdigit()]
        visited_digits = {pos: False for pos in adj_digits}
        numbers = []
        for digit in adj_digits:
            number = process_number(visited_digits, digit)
            if number > 0:
                numbers.append(number)
        if len(numbers) == 2:
            sum += reduce(lambda x, y: x * y, numbers)
    return sum

with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]
    print(part1(grid)) # 535078
    print(part2(grid)) # 75312571