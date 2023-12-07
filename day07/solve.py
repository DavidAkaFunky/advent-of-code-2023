from collections import Counter
from functools import reduce

order_part1 = {k: str(i).zfill(2) for i, k in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])}
order_part2 = {k: str(i).zfill(2) for i, k in enumerate(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])}
hand_types = ["1", "1P", "2P", "3", "FH", "4", "5"]

def get_order_part1(cards):
    return "".join((order_part1[x]) for x in cards[0])

def get_order_part2(cards):
    return "".join((order_part2[x]) for x in cards[0])

def solve(lines, part):
    get_order = get_order_part1 if part == 1 else get_order_part2
    ordered_hands = {hand_type: [] for hand_type in hand_types}
    
    for line in lines:
        counts = Counter(line[0])
        
        if part == 2:
            j_count = counts.pop("J", 0)
            if j_count == 5:
                ordered_hands["5"].append(line)
                continue
            
        counts = counts.most_common()
        most_common_count = counts[0][1]
        if part == 2:
            most_common_count += j_count
            
        if most_common_count == 3:
            hand_type = "FH" if counts[1][1] == 2 else "3"
        elif most_common_count == 2:
            hand_type = "2P" if counts[1][1] == 2 else "1P"
        else:
            hand_type = str(most_common_count)
            
        ordered_hands[hand_type].append(line)
        
    final = list(reduce(lambda x, y: x + y, [sorted(ordered_hands[hand], key=get_order, reverse=True) for hand in ordered_hands]))

    sum = 0
    for i in range(len(final)):
        sum += (i + 1) * final[i][1]
    return sum

with open("input.txt", "r") as f:
    lines = []
    for line in f.readlines():
        line = line.split()
        lines.append([line[0], int(line[1])])
    print(solve(lines, 1))
    print(solve(lines, 2))