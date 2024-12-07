import time
with open("input", "r") as f:
    grid = [l.rstrip("\n") for l in f.readlines()]

p1, p2 = 0, 0

directions = {
    "U": ((-1, 0), "R"),
    "D": ((1, 0), "L"),
    "R": ((0, 1), "D"),
    "L": ((0, -1), "U")
}
guard_start = next(((ri, ci) for ri, r in enumerate(grid) for ci, v in enumerate(r) if v == "^"))

# p1
guard, direction, visited = guard_start, "U", {}
visited[guard] = direction

while True:
    direction_offset, direction_right = directions[direction]
    next_guard = (guard[0] + direction_offset[0], guard[1] + direction_offset[1])
    if next_guard[0] < 0 or next_guard[0] > len(grid) - 1 or next_guard[1] < 0 or next_guard[1] > len(grid[next_guard[0]]) - 1:
        break
    if grid[next_guard[0]][next_guard[1]] == "#":
        direction = direction_right
    else:
        guard = next_guard

    if guard not in visited:
        visited[guard] = direction # record the first visit's direction

p1 = len(visited)
p1_visited = visited # used for optimisation in p2

# p2
for i, (ri, ci) in enumerate(p1_visited.keys()):
    if i == 0 or True:
        guard, direction, visited = guard_start, "U", set()
    else:
        last_guard = list(p1_visited.items())[i-1] # python dictionaries are ordered based on insertion yippee
        guard, direction, visited = last_guard[0], last_guard[1], set()

    visited.add((guard, direction))

    while True:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        b = time.perf_counter()
        direction_offset, direction_right = directions[direction]
        next_guard = (guard[0] + direction_offset[0], guard[1] + direction_offset[1])
        if next_guard[0] < 0 or next_guard[0] > len(grid) - 1 or next_guard[1] < 0 or next_guard[1] > len(grid[next_guard[0]]) - 1:
            break

        if grid[next_guard[0]][next_guard[1]] == "#" or (next_guard[0] == ri and next_guard[1] == ci):
            direction = direction_right
        else:
            guard = next_guard

        if (guard, direction) in visited:
            p2 += 1
            break

        visited.add((guard, direction))
        print("in took", time.perf_counter() - b)
print("p1", p1)
print("p2", p2)
