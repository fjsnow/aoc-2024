from functools import cache

with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.readlines()]

numeric = {
    (0, 0): "7", (0, 1): "8", (0, 2): "9",
    (1, 0): "4", (1, 1): "5", (1, 2): "6",
    (2, 0): "1", (2, 1): "2", (2, 2): "3",
    (3, 0): " ", (3, 1): "0", (3, 2): "A"
}

directional = {
    (0, 0): " ", (0, 1): "^", (0, 2): "A",
    (1, 0): "<", (1, 1): "v", (1, 2): ">",
}


def r(d):
    return {v: k for k, v in d.items()}


def get_paths(fr, to, pad):
    o = (to[0] - fr[0], to[1] - fr[1])
    h, v = ("<" if o[1] < 0 else ">") * \
        abs(o[1]), ("^" if o[0] < 0 else "v") * abs(o[0])

    gap = r(pad)[" "]
    if len(h) == 0 and len(v) == 0:
        return [""]
    elif len(h) == 0:
        return [v]
    elif len(v) == 0:
        return [h]
    elif (fr[0], to[1]) == gap:
        return [v + h]
    elif (to[0], fr[1]) == gap:
        return [h + v]
    else:
        return [h + v, v + h]


def get_sequences(seq, pad):
    res = []
    eseq = "A" + seq
    for i in range(len(seq)):
        k1 = eseq[i]
        k2 = eseq[i + 1]
        res += [[p + "A" for p in get_paths(r(pad)[k1], r(pad)[k2], pad)]]
    return res


@cache
def solve(line, depth, first=True):
    if depth == 0:
        return len(line)

    r = 0
    for seq in get_sequences(line, numeric if first else directional):
        r += min(
            (solve(s, depth - 1, False)
             for s in seq),
            default=0
        )

    return r


p1, p2 = 0, 0

for i, line in enumerate(inp):
    p1 += solve(line, 3) * int(line[:-1])
    p2 += solve(line, 26) * int(line[:-1])

print("p1:", p1)
print("p2:", p2)
