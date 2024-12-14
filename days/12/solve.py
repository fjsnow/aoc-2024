with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.readlines()]

seen = set()
regions = []


def ff(start):
    type_ = inp[start[0]][start[1]]

    stack = [start]
    visited = set()
    plants = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        plants.append(current)
        visited.add(current)

        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(inp) and 0 <= ny < len(inp[0]):
                if inp[nx][ny] == type_ and (nx, ny) not in visited:
                    stack.append((nx, ny))

    return {
        "type": type_,
        "plants": plants
    }


def calc_perim(plants):
    perimeter = 0
    plant_set = set(plants)
    for x, y in plants:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in plant_set:
                perimeter += 1

    return perimeter

# ugly


def calc_sides(plants):
    sides = 0

    for x, y in plants:
        neighbours = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in plants:
                neighbours.append((dx, dy))

        if len(neighbours) == 0:
            sides += 4
        elif len(neighbours) == 1:
            sides += 2
        elif len(neighbours) == 2:
            if ((-1, 0) in neighbours and (1, 0) in neighbours) or ((0, -1) in neighbours and (0, 1) in neighbours):
                continue
            sides += 1
            if (x + neighbours[0][0] + neighbours[1][0], y + neighbours[0][1] + neighbours[1][1]) not in plants:
                sides += 1
        elif len(neighbours) == 3:
            if (-1, 0) not in neighbours:
                if (x + 1, y - 1) not in plants:
                    sides += 1
                if (x + 1, y + 1) not in plants:
                    sides += 1
            elif (1, 0) not in neighbours:
                if (x - 1, y - 1) not in plants:
                    sides += 1
                if (x - 1, y + 1) not in plants:
                    sides += 1
            elif (0, 1) not in neighbours:
                if (x + 1, y - 1) not in plants:
                    sides += 1
                if (x - 1, y - 1) not in plants:
                    sides += 1
            elif (0, -1) not in neighbours:
                if (x + 1, y + 1) not in plants:
                    sides += 1
                if (x - 1, y + 1) not in plants:
                    sides += 1
        elif len(neighbours) == 4:
            if (x - 1, y - 1) not in plants:
                sides += 1
            if (x + 1, y - 1) not in plants:
                sides += 1
            if (x - 1, y + 1) not in plants:
                sides += 1
            if (x + 1, y + 1) not in plants:
                sides += 1

    return sides


p1, p2 = 0, 0

for li, line in enumerate(inp):
    for ci, char in enumerate(line):
        if (li, ci) in seen:
            continue
        region = ff((li, ci))
        for plant in region["plants"]:
            seen.add(plant)

        area = len(region["plants"])
        perim = calc_perim(region["plants"])
        sides = calc_sides(region["plants"])

        p1 += area * perim
        p2 += area * sides

print("p1", p1)
print("p2", p2)
