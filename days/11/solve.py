from collections import defaultdict

with open("input", "r") as f:
    inp = f.read().rstrip("\n")

stones = {int(s): 1 for s in inp.split(" ")}
p1, p2 = 0, 0

for i in range(75):
    ns = defaultdict(int)
    for s, f in stones.items():
        if s == 0:
            ns[1] += f 
        elif len(str(s)) % 2 == 0:
            lh, rh = str(s)[:len(str(s))//2], str(s)[len(str(s))//2:]
            ns[int(lh)] += f
            ns[int(rh)] += f 
        else:
            ns[s * 2024] += f

    stones = ns
    if i == 24:
        p1 = sum(stones.values())

p2 = sum(stones.values())

print("p1:", p1)
print("p2:", p2)
