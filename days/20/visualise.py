import os
import sys
import time

with open("input", "r") as f:
    grid = [l.rstrip("\n") for l in f.readlines()]

start = next((y, x) for y, row in enumerate(grid)
             for x, val in enumerate(row) if val == "S")


def gray(s, amount):
    return f"\x1b[38;5;{240 + amount}m{s}\x1b[0m"


def green(s):
    return f"\x1b[38;5;46m{s}\x1b[0m"


def red(s):
    return f"\x1b[38;5;196m{s}\x1b[0m"


def update(x, y, s):
    print(f"\033[{x+1};{y+1}H{s}", end="")


def clear(xys, exys=[]):
    for x, y in xys:
        if (x, y) not in exys:
            update(x, y, " ")


os.system("clear")
print("\033[?25l")
for ri, row in enumerate(grid):
    for ci, val in enumerate(row):
        if val == "#":
            update(ri, ci, gray(val, 0))

sys.stdout.flush()
dist = {start: 0}
q = [start]
update(start[0], start[1], ".")
while q:
    x, y = q.pop()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in dist:
            continue
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[dx]):
            continue
        if grid[nx][ny] == "#":
            continue
        dist[(nx, ny)] = dist[(x, y)] + 1
        q.append((nx, ny))

p1, p2 = 0, 0
update(0, len(grid[0]) + 2, f"p1: 0")
update(1, len(grid[0]) + 2, f"p2: 0")

ld = []
for (x, y), d in dist.items():
    clear(ld)
    ld = []
    update(x, y, "@")
    ld.append((x, y))
    for i in range(-20, 21):
        for j in range(-20, 21):
            if (i, j) == (0, 0):
                continue
            cd = abs(i) + abs(j)
            if cd > 20:
                continue
            dx, dy = x+i, y+j
            if (dx, dy) in dist:
                nd = dist[(dx, dy)] + cd
                ld.append((dx, dy))
                if d - nd < 100:
                    update(dx, dy, red("."))
                    continue
                update(dx, dy, green("."))
                if cd == 2:
                    p1 += 1
                if cd <= 20:
                    p2 += 1

                update(0, len(grid[0]) + 2, f"p1: {p1}")
                update(1, len(grid[0]) + 2, f"p2: {p2}")

    sys.stdout.flush()
