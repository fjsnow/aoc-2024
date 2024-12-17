import sys

if len(sys.argv) > 1 and sys.argv[1] == "-r":
    with open("input", "r") as f:
        inp = [l.rstrip("\n") for l in f.read().split("\n\n")]
    print(f"----- USING REAL INPUT -----")
else:
    option = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    inp = [
        """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""",
        """""",
        """""",
        """""",
        """""",
    ][option].split("\n\n")
    print(f"----- USING EXAMPLE INPUT #{option} -----")

registers = {name[-1]: int(num) for name, num in [reg.split(": ")
                                                  for reg in inp[0].split("\n")]}

instructions = [int(x) for x in inp[1].split(": ")[1].split(",")]


def get_combo_value(operand):
    if 0 <= operand <= 3:
        return operand
    elif 4 <= operand <= 6:
        return {4: registers["A"], 5: registers["B"], 6: registers["C"]}[operand]
    raise Exception("What the sigma")


ip = 0
out = []


def execute(operator, operand):
    global ip
    if operator == 0:  # adv
        registers["A"] = registers["A"] // (2 ** get_combo_value(operand))
    elif operator == 1:  # bxl
        registers["B"] = registers["B"] ^ operand
    elif operator == 2:  # bst
        registers["B"] = get_combo_value(operand) % 8
    elif operator == 3:  # jnz
        if registers["A"] != 0:
            ip = operand - 2
    elif operator == 4:  # bxc
        registers["B"] = registers["B"] ^ registers["C"]
    elif operator == 5:  # out
        out.append(get_combo_value(operand) % 8)
    elif operator == 6:  # bdv
        registers["B"] = registers["A"] // (2 ** get_combo_value(operand))
    elif operator == 7:  # cdv
        registers["C"] = registers["A"] // (2 ** get_combo_value(operand))


while ip < len(instructions):
    operator = instructions[ip]
    operand = instructions[ip + 1]
    execute(operator, operand)
    ip += 2

# 2,4 B <- A % 8
# 1,5 B <- B ^ 5
# 7,5 C <- A // (2^B)
# 1,6 B <- B ^ 6
# 4,1 B <- B ^ C
# 5,5 out B % 8
# 0,3 A <- A // (2^3)
# 3,0 ip = 0 (unless A = 0)

# 2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0

# out 0

print(','.join([str(x) for x in out]))
