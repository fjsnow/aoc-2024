from collections import defaultdict

with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.readlines()]

connections = defaultdict(list)
for li, line in enumerate(inp):
    o, t = line.split("-")
    connections[o].append(t)
    connections[t].append(o)

# p1
interconnected = set()
for a in connections.keys():
    for b in connections[a]:
        for c in connections[b]:
            if a not in connections[c]:
                continue
            if 't' not in a[0] + b[0] + c[0]:
                continue
            interconnected.add(frozenset({a, b, c}))

# p2
all_connections = set()
for a in connections.keys():
    ac = set([a])
    for b, bc in connections.items():
        for c in ac:
            if c not in bc:
                break
        else:
            ac.add(b)
    all_connections.add(frozenset(ac))


print("p1:", len(interconnected))
print("p2:", ','.join(sorted(max(all_connections, key=lambda x: len(x)))))
