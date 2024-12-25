def meta():
    return {
        "title": "Ceres Search",
        "solutions": {
            "a": 2297,
            "b": 1745
        }
    }

def parse(input):
    return input.split("\n")

def is_present(grid, coord, dir, word):
    letters = grid[coord[0]][coord[1]]
    for _ in range(len(word) - 1):
        coord[0] += dir[0]
        coord[1] += dir[1]
        if coord[0] < 0 or coord[0] > len(grid) - 1 or coord[1] < 0 or coord[1] > len(grid[coord[0]]) - 1:
            break
        letters += grid[coord[0]][coord[1]]
    return letters == word


directions = [(0, -1), (0, 1), (-1, 0), (1, 0),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]
x_pairs = {
    (-1, -1): [(1, -1), (-1, 1)],
    (-1, 1): [(-1, -1), (1, 1)],
    (1, -1): [(-1, -1), (1, 1)],
    (1, 1): [(1, -1), (-1, 1)]
}

def a(grid):
    a = 0
    for ri, row in enumerate(grid):
        for ci, _ in enumerate(row):
            for d in directions:
                if is_present(grid, [ri, ci], d, "XMAS"):
                    a += 1
    return a


def b(grid):
    centers = []
    for ri, row in enumerate(grid):
        for ci, _ in enumerate(row):
            for d in directions:
                if is_present(grid, [ri, ci], d, "MAS"):
                    centers.append(((ri + d[0], ci + d[1]), d))

    b = 0
    for (ri, ci), d1 in centers:
        for d2 in x_pairs.get(d1, []):
            if ((ri, ci), d2) in centers:
                b += 1

    return b // 2
