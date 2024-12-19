from functools import cache

with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.read().split("\n\n")]

patterns = inp[0].split(", ")


def solve(towel, p2):
    if len(towel) == 0:
        return 1
    c = 0
    for p in patterns:
        if towel[:len(p)] == p:
            n = solve(towel[len(p):], p2)
            if p2:
                c += n if p2 else (1 if n == 1 else 0)
            elif n == 1:
                c += 1
                break
    return c


print("p1:", sum(solve(t, False) for t in inp[1].split("\n")))
print("p2:", sum(solve(t, True) for t in inp[1].split("\n")))
