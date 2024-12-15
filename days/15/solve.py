with open("input", "r") as f:
    inp = f.read().split("\n\n")

grid = inp[0].split("\n")
moves = ''.join(inp[1].split("\n"))


def get_moved_tiles(grid, player, dir):
    if dir[1] != 0:  # horizontal
        to_move = []
        curr = player
        while True:
            if grid[curr[0]][curr[1]] == ".":
                return to_move
            elif grid[curr[0]][curr[1]] == "#":
                return []

            to_move.append(curr)
            curr = (curr[0] + d[0], curr[1] + d[1])
    else:  # vertical
        to_move = []
        processing = [player]
        while True:
            if len(processing) == 0:
                return to_move
            if len(processing) > 0:
                curr = processing.pop()
                if grid[curr[0]][curr[1]] == "#":
                    return []
                elif grid[curr[0]][curr[1]] == ".":
                    continue
                to_move.append(curr)
                processing.append((curr[0] + d[0], curr[1] + d[1]))
                if grid[curr[0]][curr[1]] == "[":
                    if grid[curr[0]][curr[1] + 1] == "#":
                        return []
                    to_move.append((curr[0], curr[1] + 1))
                    processing.append(
                        (curr[0] + d[0], curr[1] + d[1] + 1))
                if grid[curr[0]][curr[1]] == "]":
                    processing.append((curr[0], curr[1] - 1))
                    if grid[curr[0]][curr[1] - 1] == "#":
                        return []
                    to_move.append((curr[0], curr[1] - 1))
                    processing.append(
                        (curr[0] + d[0], curr[1] + d[1] - 1))


stretched = []
for ri, row in enumerate(grid):
    stretched_row = []
    for ci, val in enumerate(row):
        if val == "#":
            stretched_row.extend(["#", "#"])
        if val == "O":
            stretched_row.extend(["[", "]"])
        if val == ".":
            stretched_row.extend([".", "."])
        if val == "@":
            stretched_row.extend(["@", "."])
    stretched.append(stretched_row)

player = None
for ri, row in enumerate(stretched):
    for ci, val in enumerate(row):
        if val == "@":
            player = (ri, ci)

for move in moves:
    d = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}[move]
    tiles = get_moved_tiles(stretched, player, d)
    original = [row.copy() for row in stretched]

    player_moved = False
    for tile in tiles:
        if tile == player and not player_moved:
            player = (tile[0] + d[0], tile[1] + d[1])
            player_moved = True

        stretched[tile[0] + d[0]][tile[1] + d[1]] = original[tile[0]][tile[1]]
        if (tile[0] - d[0], tile[1] - d[1]) not in tiles:
            stretched[tile[0]][tile[1]] = "."

p2 = 0
for ri, row in enumerate(stretched):
    for ci, val in enumerate(row):
        if val == "[":
            p2 += ri * 100 + ci

print("p2:", p2)
