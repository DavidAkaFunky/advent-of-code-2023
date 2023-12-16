def hash(step):
    value = 0
    for char in step:
        value = ((value + ord(char)) * 17) % 256
    return value

def part1(steps):
    return sum(hash(step) for step in steps)

def part2(steps):
    boxes = {}
    for step in steps:
        if "=" in step:
            label, op, lens = step[:-2], step[-2], step[-1]
        else:
            label, op = step[:-1], step[-1]
        box = hash(label)
        if box not in boxes:
            boxes[box] = {}
        if op == "=":
            boxes[box][label] = lens
        elif label in boxes[box]:
            del boxes[box][label]
    return sum((box + 1) * (i + 1) * int(boxes[box][label]) for box in boxes for i, label in enumerate(boxes[box]))
        
with open("input.txt", "r") as f:
    steps = f.read().split(",")
    print(part1(steps))
    print(part2(steps))