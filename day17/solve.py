import heapq
from time import sleep

opposite_dir = {"N": "S", "S": "N", "E": "W", "W": "E"}
    
def get_loss(lines, pos):
    return int(lines[pos[0]][pos[1]])

def get_new_pos(pos, _dir):
    match _dir:
        case "N":
            return (pos[0] - 1, pos[1])
        case "S":
            return (pos[0] + 1, pos[1])
        case "E":
            return (pos[0], pos[1] + 1)
        case "W":
            return (pos[0], pos[1] - 1)

def solve(lines, max_seq_len, min_seq_len=0):
    max_i = len(lines) - 1
    max_j = len(lines[0]) - 1
    pq = []
    visited = set()
    # Loss, (i, j), direction, sequence length
    heapq.heappush(pq, (0, (0, 0), "E", 1))
    heapq.heappush(pq, (0, (0, 0), "S", 1))
    while pq:
        node = heapq.heappop(pq)
        if node[1:] in visited:
            continue
        loss, pos, dir_, seq_len = node
        pos = get_new_pos(pos, dir_)
        if not (0 <= pos[0] <= max_i and 0 <= pos[1] <= max_j):
            continue
        loss += get_loss(lines, pos)
        if pos == (max_i, max_j):
            return loss
        visited.add(node[1:])
        for d in "NSEW":
            if d == opposite_dir[dir_]:
                continue
            if d == dir_:
                new_seq_len = seq_len + 1
                if new_seq_len > max_seq_len:
                    continue
            else:
                if seq_len < min_seq_len:
                    continue
                new_seq_len = 1
            new_node = (loss, pos, d, new_seq_len)
            heapq.heappush(pq, new_node)


with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    print(solve(lines, 3))
    print(solve(lines, 10, min_seq_len=4))