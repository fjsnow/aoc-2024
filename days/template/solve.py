import sys

if len(sys.argv) > 1 and sys.argv[1] == "-r":
    with open("input", "r") as f:
        inp = [l.rstrip("\n") for l in f.readlines()]
    print(f"----- USING REAL INPUT -----")
else:
    option = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    inp = [
        """""",
        """""",
        """""",
        """""",
        """""",
    ][option].split("\n")
    print(f"----- USING EXAMPLE INPUT #{option} -----")
    print('\n'.join(inp))

total = 0

for li, line in enumerate(inp):
    # for ci, char in enumerate(line):
    #     pass
    # for vi, val in enumerate(line.split(" ")):
    #     pass
    pass

print("total:", total)
