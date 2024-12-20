with open("input", "r") as f:
    grid = [l.rstrip("\n") for l in f.readlines()]

start = next((y, x) for y, row in enumerate(grid)
             for x, val in enumerate(row) if val == "S")

dist = {start: 0}
q = [start]
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
cheats = 20

for (x, y), d in dist.items():
    for i in range(-20, 21):
        for j in range(-20, 21):
            cd = abs(i) + abs(j)
            if cd > cheats:
                continue
            dx, dy = x+i, y+j
            if (dx, dy) in dist:
                nd = dist[(dx, dy)] + cd
                if d - nd < 100:
                    continue
                if cd == 2:
                    p1 += 1
                if cd <= 20:
                    p2 += 1

print("p1", p1)
print("p2", p2)
