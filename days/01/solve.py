with open("input", "r") as f:
    input = [l.rstrip("\n") for l in f.readlines()]

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
