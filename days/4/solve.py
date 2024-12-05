with open("input", "r") as f:
    input = [l.rstrip("\n") for l in f.readlines()]

p1, p2 = 0, 0

directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
x_pairs = {
    (-1, -1): [(1, -1), (-1, 1)],
    (-1, 1): [(-1, -1), (1, 1)],
    (1, -1): [(-1, -1), (1, 1)],
    (1, 1): [(1, -1), (-1, 1)]
}

def is_present(c, direction, word):
    letters = input[c[0]][c[1]]
    for _ in range(len(word) - 1):
        c[0] += direction[0]
        c[1] += direction[1]
        if c[0] < 0 or c[0] > len(input) - 1 or c[1] < 0 or c[1] > len(input[c[0]]) - 1:
            break
        letters += input[c[0]][c[1]]
    return letters == word

centers = []
for li, line in enumerate(input):
    for ci, char in enumerate(line):
        for d in directions:
            if is_present([li, ci], d, "XMAS"):
                p1 += 1
            if is_present([li, ci], d, "MAS"):
                centers.append((li + d[0], ci + d[1], d))

for li, ci, d1 in centers:
    for d2 in x_pairs.get(d1, []):
        if (li, ci, d2) in centers:
            p2 += 1

print("p1:", p1)
print("p2:", p2 // 2)
