with open("input", "r") as f:
    grid = [l.rstrip("\n") for l in f.readlines()]

p1, p2 = 0, 0

starts = [(ri, vi) for ri, row in enumerate(grid) for vi, val in enumerate(row) if val == "0"]
for start in starts:
    q, seen = [start], set()
    while q:
        curr = q.pop()
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n = (curr[0] + d[0], curr[1] + d[1])
            if (
                n[0] < 0 or n[1] < 0 or
                n[0] >= len(grid) or n[1] >= len(grid[0]) or
                grid[n[0]][n[1]] == "." or
                int(grid[n[0]][n[1]]) - int(grid[curr[0]][curr[1]]) != 1
            ):
                continue

            if grid[n[0]][n[1]] == "9":
                p2 += 1
                if n not in seen:
                    p1 += 1
                    seen.add(n)
            else:
                q.append(n)

print("p1:", p1)
print("p2:", p2)

