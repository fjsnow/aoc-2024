import heapq

with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.readlines()]

corrupted = []
for line in inp:
    x, y = [int(x) for x in line.split(",")]
    corrupted.append((x, y))

for i in range(1024, len(corrupted)):
    q = [(0, (0, 0))]
    heapq.heapify(q)
    b = set()
    while len(q) > 0:
        c, (cx, cy) = heapq.heappop(q)
        if (cx, cy) == (70, 70):
            if i == 1024:
                print("p1:", c)
            break
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in b:
                continue
            if nx < 0 or ny < 0 or nx > 70 or ny > 70:
                continue
            if (nx, ny) in corrupted[:i]:
                continue
            heapq.heappush(q, (c+1, (nx, ny)))
            b.add((nx, ny))
    else:
        print("p2:", f"{corrupted[i-1][0]},{corrupted[i-1][1]}")
        break
