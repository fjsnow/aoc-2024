import os
with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.readlines()]

BOARD_SIZE = (103, 101)


def visualise(robots, show_quadrants=True):
    for x in range(BOARD_SIZE[0]):
        for y in range(BOARD_SIZE[1]):
            if show_quadrants and (y == BOARD_SIZE[0] // 2 or x == BOARD_SIZE[1] // 2):
                print("#", end="")
                continue
            for r in robots:
                if r[0][1] == x and r[0][0] == y:
                    print("*", end="")
                    break
            else:
                print(" ", end="")
        print("")


def calculate_safety_score(robots):
    quads = [0, 0, 0, 0]
    for robot in robots:
        ((x, y), _) = robot
        if x == BOARD_SIZE[1] // 2 or y == BOARD_SIZE[0] // 2:
            continue
        home = 0
        if x > BOARD_SIZE[1] // 2:
            home += 1
        if y > BOARD_SIZE[0] // 2:
            home += 2
        quads[home] += 1

    res = 1
    for q in quads:
        res *= q

    return res


robots = []
for li, line in enumerate(inp):
    p, v = line.split(" ")
    px, py = [int(x) for x in p.split("=")[1].split(",")]
    vx, vy = [int(x) for x in v.split("=")[1].split(",")]
    robots.append(((px, py), (vx, vy)))

# part 1

one_robots = robots.copy()
for ri, robot in enumerate(one_robots):
    (px, py), (vx, vy) = robot
    px = (px + 100 * vx) % BOARD_SIZE[1]
    py = (py + 100 * vy) % BOARD_SIZE[0]
    one_robots[ri] = ((px, py), (vx, vy))

p1 = calculate_safety_score(one_robots)

# part 2

states = []
for step in range(BOARD_SIZE[0] * BOARD_SIZE[1]):
    for ri, robot in enumerate(robots):
        (px, py), (vx, vy) = robot
        px = (px + vx) % BOARD_SIZE[1]
        py = (py + vy) % BOARD_SIZE[0]
        robots[ri] = ((px, py), (vx, vy))
    states.append((step, robots.copy(), calculate_safety_score(robots)))

states.sort(key=lambda x: x[2])
chosen = 0
while True:
    os.system("clear")
    visualise(states[chosen][1])

    print("")
    if chosen != 0:
        print("[P]revious, ", end="")
    if chosen != len(states) - 1:
        print("[N]ext, ", end="")
    print("[D]one", end="")
    choice = input(": ")
    if chosen != 0 and choice.upper() == "P":
        chosen -= 1
    elif chosen != len(states) - 1 and choice.upper() == "N":
        chosen += 1
    elif choice.upper() == "D":
        break

os.system("clear")
print("p1:", p1)
print("p2:", states[chosen][0] + 1)
