import heapq

with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.readlines()]

DIRECTIONS = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
TURNS = {
    "N": ["W", "E"],
    "E": ["N", "S"],
    "S": ["W", "E"],
    "W": ["N", "S"]
}

deers = []
goal = None

for ri, row in enumerate(inp):
    for ci, val in enumerate(row):
        if val == "S":
            deers.append((0, (ri, ci), "E", set()))
        elif val == "E":
            goal = (ri, ci)

assert goal is not None

heapq.heapify(deers)
min = {}

best = float('inf')
good = set()

while len(deers) > 0:
    cost, pos, dir, been = heapq.heappop(deers)
    if (pos, dir) in min and min[(pos, dir)] < cost:
        if pos == goal:
            break
        else:
            continue

    if pos == goal:
        if cost <= best:
            best = cost
            for pos, _ in been:
                good.add(pos)
            continue

    min[(pos, dir)] = cost

    been = been.copy()
    been.add((pos, dir))

    next_pos = (pos[0] + DIRECTIONS[dir][0], pos[1] + DIRECTIONS[dir][1])
    if inp[next_pos[0]][next_pos[1]] != "#":
        if (next_pos, dir) not in min or min[(next_pos, dir)] > cost + 1:
            heapq.heappush(deers, (cost + 1, next_pos, dir, been))

    for d in TURNS[dir]:
        if (pos, d) not in min or min[(pos, d)] > cost + 1000:
            heapq.heappush(deers, (cost + 1000, pos, d, been))

print("p2", len(good) + 1)
