with open("input", "r") as f:
    grid = [l.rstrip("\n") for l in f.readlines()]

p1, p2 = 0, 0

ds = { "U": (-1, 0, "R"), "D": (1, 0, "L"), "R": (0, 1, "D"), "L": (0, -1, "U") }
gs = next(((ri, ci) for ri, r in enumerate(grid) for ci, v in enumerate(r) if v == "^"))

# p1
g, d, vi, vid = gs, "U", set(), []
vi.add(g)
while True:
    n = (g[0] + ds[d][0], g[1] + ds[d][1])
    if n[0] < 0 or n[0] > len(grid) - 1 or n[1] < 0 or n[1] > len(grid[n[0]]) - 1:
        break
    if grid[n[0]][n[1]] == "#":
        d = ds[d][2]
    else:
        g = n
    if g not in vi:
        vi.add(g)
        vid.append((g, d))
p1 = len(vi)

pvid = vid
# p2
for i, ((ri, ci), d) in enumerate(pvid):
    if i == 0:
        g, d, vid = gs, "U", set()
    else:
        l = pvid[i-1]
        g, d, vid = l[0], l[1], set()
    vi.add((g, d))
    while True:
        n = (g[0] + ds[d][0], g[1] + ds[d][1])
        if n[0] < 0 or n[0] > len(grid) - 1 or n[1] < 0 or n[1] > len(grid[n[0]]) - 1:
            break
        if grid[n[0]][n[1]] == "#" or (n[0] == ri and n[1] == ci):
            d = ds[d][2]
        else:
            g = n
        if (g, d) in vid:
            p2 += 1
            break
        vid.add((g, d))

print("p1", p1)
print("p2", p2)
