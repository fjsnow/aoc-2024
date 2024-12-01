import sys

if len(sys.argv) > 1 and sys.argv[1] == "-r":
    with open("input", "r") as f:
        input = [l.rstrip("\n") for l in f.readlines()]
else:
    input = """3   4
4   3
2   5
1   3
3   9
3   3""".split("\n")

p1, p2 = 0, 0

l, r = [], []
for line in input:
    l.append(int(line.split("   ")[0]))
    r.append(int(line.split("   ")[1]))

l.sort()
r.sort()

for le, re in zip(l, r):
    p1 += max(le, re) - min(le, re)
    p2 += le * r.count(le)

print("p1:", p1)
print("p2:", p2)
