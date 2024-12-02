import sys

if len(sys.argv) > 1 and sys.argv[1] == "-r":
    with open("input", "r") as f:
        input = [l.rstrip("\n") for l in f.readlines()]
else:
    input = """""".split("\n")

total = 0

for li, line in enumerate(input):
    # for ci, char in enumerate(line):
    #     pass
    # for vi, val in enumerate(line.split("\n")):
    #     pass
    pass

print("total:", total)
