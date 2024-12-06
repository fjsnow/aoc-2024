with open("input", "r") as f:
    grid = [l.rstrip("\n") for l in f.readlines()]

p1, p2 = 0, 0

ds = { "U": (-1, 0, "R"), "D": (1, 0, "L"), "R": (0, 1, "D"), "L": (0, -1, "U") }
gs = next(((ri, ci) for ri, r in enumerate(grid) for ci, v in enumerate(r) if v == "^"))

# p1
g, d, v = gs, "U", set()
v.add(g)
while True:
    n = (g[0] + ds[d][0], g[1] + ds[d][1])
    if n[0] < 0 or n[0] > len(grid) - 1 or n[1] < 0 or n[1] > len(grid[n[0]]) - 1:
        break
    if grid[n[0]][n[1]] == "#":
        d = ds[d][2]
    else:
        g = n
    v.add(g)
p1 = len(v)

# p2
for ri, r in enumerate(grid):
    for ci, v in enumerate(r):
        if v == "#":
            continue
        g, d, v = gs, "U", set()
        v.add((g, d))
        while True:
            n = (g[0] + ds[d][0], g[1] + ds[d][1])
            if n[0] < 0 or n[0] > len(grid) - 1 or n[1] < 0 or n[1] > len(grid[n[0]]) - 1:
                break
            if grid[n[0]][n[1]] == "#" or (n[0] == ri and n[1] == ci):
                d = ds[d][2]
            else:
                g = n
            if (g, d) in v:
                p2 += 1
                break
            v.add((g, d))

print("p1", p1)
print("p2", p2)
