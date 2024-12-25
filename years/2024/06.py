def meta():
    return {
        "title": "Guard Gallivant",
        "solutions": {
            "a": 5318,
            "b": 1831
        }
    }

def parse(input):
    grid = input.split("\n")
    start = next(((ri, ci) for ri, r in enumerate(grid)
                  for ci, v in enumerate(r) if v == "^"))
    return (grid, start)


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def shared(input):
    grid, start = input
    pos, dir, been = start, 0, {start: 0}
    while True:
        next_pos = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(grid) or next_pos[1] >= len(grid[next_pos[0]]):
            break
        if grid[next_pos[0]][next_pos[1]] == "#":
            dir = (dir + 1) % len(directions)
        else:
            pos = next_pos

        if pos not in been:
            been[pos] = dir

    return been


def a(input):
    return len(shared(input))

def b(input):
    grid, start = input
    a = shared(input)
    b = 0

    for i, (ri, ci) in enumerate(a.keys()):
        if i == 0:
            pos, dir, been = start, 0, set()
        else:
            last = list(a.items())[i - 1]
            pos, dir, been = last[0], last[1], set()
        been.add((pos, dir))

        while True:
            next_pos = (pos[0] + directions[dir][0],
                        pos[1] + directions[dir][1])
            if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(grid) or next_pos[1] >= len(grid[next_pos[0]]):
                break
            if grid[next_pos[0]][next_pos[1]] == "#" or next_pos == (ri, ci):
                dir = (dir + 1) % len(directions)
            else:
                pos = next_pos

            if (pos, dir) in been:
                b += 1
                break

            been.add((pos, dir))

    return b
