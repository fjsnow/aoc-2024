with open("input", "r") as f:
    input = [l.rstrip("\n") for l in f.readlines()]

antennas = []
for row, line in enumerate(input):
    for col, char in enumerate(line):
        if char != ".":
            antennas.append((row, col, char))

uq1, uq2 = set(), set()
for i, ant1 in enumerate(antennas):
    for j, ant2 in enumerate(antennas[i+1:], i+1):
        if ant1[2] != ant2[2]:
            continue

        dx, dy = ant2[0] - ant1[0], ant2[1] - ant1[1]

        # backwards
        k = 0 
        while True:
            anti = (ant1[0] - dx * k, ant1[1] - dy * k)
            if anti[0] < 0 or anti[0] > len(input) - 1 or anti[1] < 0 or anti[1] > len(input[anti[0]]) - 1:
                break
            uq2.add(anti)
            if k == 1:
                uq1.add(anti)
            k += 1

        # forwards
        k = 0
        while True:
            anti = (ant2[0] + dx * k, ant2[1] + dy * k)
            if anti[0] < 0 or anti[0] > len(input) - 1 or anti[1] < 0 or anti[1] > len(input[anti[0]]) - 1:
                break
            uq2.add(anti)
            if k == 1:
                uq1.add(anti)
            k += 1

print("p1", len(uq1))
print("p2", len(uq2))
