with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.read().split("\n\n")]

locks, keys = [], []
for grid in [x.split("\n") for x in inp if x != ""]:
    lock = grid[0] == "#####"
    heights = []
    for i in range(5):
        height = -1
        for j in range(len(grid)):
            if grid[j if lock else len(grid) - j - 1][i] == ".":
                break
            height += 1
        heights.append(height)

    locks.append(heights) if lock else keys.append(heights)

fit = set()
for lock in locks:
    for key in keys:
        for i in range(5):
            if lock[i] + key[i] >= 6:
                break
        else:
            fit.add((tuple(lock), tuple(key)))

print("p1:", len(fit))
