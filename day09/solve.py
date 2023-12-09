def solve(lines):
    sum_first, sum_last = 0, 0
    for line in lines:
        levels = [[int(value) for value in line.strip().split()]]
        i = 0
        while any(map(lambda x: x != 0, levels[i])):
            levels.append([y - x for x, y in zip(levels[i], levels[i][1:])])
            i += 1
        # No need to iterate over the bottom layer (it's all 0s)
        # or the top layer (store the new values immediately in the sums)
        for i in range(len(levels) - 2, 1, -1):
            levels[i-1].append(levels[i-1][-1] + levels[i][-1])
            levels[i-1].insert(0, levels[i-1][0] - levels[i][0])
        sum_first += levels[0][0] - levels[1][0]
        sum_last += levels[0][-1] + levels[1][-1]
    return sum_last, sum_first

with open("input.txt", "r") as f:
    part1, part2 = solve(f.readlines())
    print(part1)
    print(part2)