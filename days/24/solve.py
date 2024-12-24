with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.read().split("\n\n")]

wires = {}
for wire in inp[0].split("\n"):
    name, val = wire.split(": ")
    val = int(val)
    wires[name] = val

instructions = []
for inst in inp[1].split("\n"):
    l, r = inst.split(" -> ")
    x, op, y = l.split(" ")
    instructions.append((x, op, y, r))

while instructions:
    inst = instructions.pop()
    x, op, y, r = inst
    if x not in wires or y not in wires:
        instructions.insert(0, inst)
        continue

    if op == "AND":
        wires[r] = wires[x] & wires[y]
    elif op == "OR":
        wires[r] = wires[x] | wires[y]
    elif op == "XOR":
        wires[r] = wires[x] ^ wires[y]

print(int("".join(str(val) for wire, val in sorted(wires.items(),
      key=lambda x: x[0], reverse=True) if wire[0] == "z"), 2))
