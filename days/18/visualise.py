import heapq
import sys
import os
import time

with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.readlines()]

corrupted = []
for line in inp:
    x, y = [int(x) for x in line.split(",")]
    corrupted.append((x, y))


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


def djikstra(start, corrupted, draw):
    q = [(0, start, [start])]
    heapq.heapify(q)
    b = set()
    ldraw = []
    while q:
        c, (cx, cy), h = heapq.heappop(q)
        if draw:
            cdraw = []
            for x, y in h:
                update(x, y, ".")
                cdraw.append((x, y))
            clear(ldraw, cdraw)
            sys.stdout.flush()
            ldraw = cdraw
        if (cx, cy) == (70, 70):
            return b, h
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in b:
                continue
            if nx < 0 or ny < 0 or nx > 70 or ny > 70:
                continue
            if (nx, ny) in corrupted:
                continue
            b.add((nx, ny))

            hn = h.copy()
            hn.append((nx, ny))
            heapq.heappush(q, (c+1, (nx, ny), hn))
    return b, None


START = 1024

os.system("clear")
print("\033[?25l")
for x, y in corrupted[:START]:
    update(x, y, gray("#", 0))
sys.stdout.flush()

l = None
for i in range(START, len(corrupted)):
    update(72, 0, f"corrupted: {i}")
    update(corrupted[i-1][0], corrupted[i-1][1], gray("#", 10))
    update(corrupted[i-2][0], corrupted[i-2][1], gray("#", 0))
    sys.stdout.flush()

    if l is not None and l[1] is not None and corrupted[i-1] not in l[1]:
        time.sleep(0.01)  # otherwise you can't see
        continue
    else:
        if l is not None:
            clear(l[1], corrupted[:i])
        r = djikstra((0, 0), corrupted[:i], True)
        if r[1] is not None:
            for x, y in r[1]:
                update(x, y, green("."))
                sys.stdout.flush()
        else:
            if l is not None:
                clear(l[0], corrupted[:i])
                for x, y in r[0]:
                    update(x, y, red("."))
                sys.stdout.flush()
            break
        l = r

input()
