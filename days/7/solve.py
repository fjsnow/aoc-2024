with open("input", "r") as f:
    input = [l.rstrip("\n") for l in f.readlines()]

def is_goal_possible(goal, numbers, p2):
    evals = [numbers[0]]
    for n in numbers[1:]:
        next_evals = []
        for eval in evals:
            plus, times, concat = eval + n, eval * n, int(f"{eval}{n}")
            if plus <= goal:
                next_evals.append(plus)
            if times <= goal:
                next_evals.append(times)
            if concat <= goal and p2:
                next_evals.append(concat)
        evals = next_evals
    return goal in evals

p1, p2 = 0, 0
for li, line in enumerate(input):
    parts = line.split(": ")
    goal, numbers = int(parts[0]), [int(n) for n in parts[1].split(" ")]
    p1 += goal if is_goal_possible(goal, numbers, False) else 0
    p2 += goal if is_goal_possible(goal, numbers, True) else 0

print("p1", p1)
print("p2", p2)
