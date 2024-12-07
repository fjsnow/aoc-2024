with open("input", "r") as f:
    input = [l.rstrip("\n") for l in f.readlines()]

def is_goal_possible(goal, numbers, p2):
    stack = [(numbers[0], 0)]
    while stack:
        current, index = stack.pop()
        if index == len(numbers) - 1:
            if current == goal:
                return True
            continue

        number = numbers[index + 1]

        plus = current + number 
        if plus <= goal:
            stack.append((plus, index + 1))
        times = current * number 
        if times <= goal:
            stack.append((times, index + 1))
        if p2:
            concat = current * (10 ** len(str(number))) + number
            if concat <= goal:
                stack.append((concat, index + 1))
    return False


p1, p2 = 0, 0
for li, line in enumerate(input):
    parts = line.split(": ")
    goal, numbers = int(parts[0]), [int(n) for n in parts[1].split(" ")]
    p1 += goal if is_goal_possible(goal, numbers, False) else 0
    p2 += goal if is_goal_possible(goal, numbers, True) else 0

print("p1", p1)
print("p2", p2)
