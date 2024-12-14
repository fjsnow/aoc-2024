import time

with open("input", "r") as f:
    inp = f.read().rstrip()

starting = [(i // 2, int(c), False) if i % 2 == 0 else (".", int(c), False) for i, c in enumerate(inp)]

def checksum(blocks):
    c, pos = 0, 0
    for bt, count, _ in blocks:
        if bt == ".":
            pos += count
            continue
        for _ in range(count):
            c += bt * pos
            pos += 1
    return c

def solve(blocks, p2):
    while True:
        ri = next((i for i, (block_type, _, p) in reversed(list(enumerate(blocks))) if block_type != "." and not (p2 and p)), None)
        if ri is None:
            break

        li = next((i for i, (block_type, count, _) in enumerate(blocks) if block_type == "." and (not p2 or count >= blocks[ri][1])), None)
        if not p2 and li is not None and li >= ri:
            break
        if li is None or li >= ri:
            blocks[ri] = (blocks[ri][0], blocks[ri][1], True)
            continue

        lc = blocks[li][1]
        if p2:
            blocks[li] = (blocks[ri][0], blocks[ri][1], True)
            blocks[ri] = (".", blocks[ri][1], False)
            if blocks[li][1] < lc:
                blocks.insert(li+1, (".", lc - blocks[li][1], False))
        else:
            mm = min(blocks[li][1], blocks[ri][1])
            if blocks[li][1] >= blocks[ri][1]:
                blocks[li] = (blocks[ri][0], mm, False)
                blocks[ri] = (".", blocks[ri][1], False)
                blocks.insert(li+1, (".", lc - mm, False))
            else:
                blocks[li] = (blocks[ri][0], mm, True)
                blocks[ri] = (blocks[ri][0], blocks[ri][1] - mm, False)

    return checksum(blocks)

b = time.perf_counter()
print("p1:", solve(starting.copy(), False), "(", time.perf_counter() - b, " s)")
b = time.perf_counter()
print("p2:", solve(starting.copy(), True), "(", time.perf_counter() - b, " s)")
