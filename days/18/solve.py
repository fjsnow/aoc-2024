import heapq

with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.readlines()]

corrupted = []
for line in inp:
    x, y = [int(x) for x in line.split(",")]
    corrupted.append((x, y))


def djikstra(start, corrupted):
    q = [(0, start)]
    heapq.heapify(q)
    b = set()
    while q:
        c, (cx, cy) = heapq.heappop(q)
        if (cx, cy) == (70, 70):
            return c, (cx, cy)
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in b:
                continue
            if nx < 0 or ny < 0 or nx > 70 or ny > 70:
                continue
            if (nx, ny) in corrupted:
                continue
            b.add((nx, ny))

            heapq.heappush(q, (c+1, (nx, ny)))
    return None


first = djikstra((0, 0), corrupted[:1024])
assert first is not None

print("p1:", first[0])

low, high = 1024, len(corrupted)
while low < high:
    mid = (low + high) // 2
    result = djikstra((0, 0), corrupted[:mid])
    if result is None:
        high = mid - 1
    else:
        low = mid + 1

print("p2:", corrupted[low])
