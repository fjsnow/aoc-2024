with open("input", "r") as f:
    inp = [l.rstrip("\n") for l in f.read().split("\n\n")]

instructions = [int(x) for x in inp[1].split(": ")[1].split(",")]
registers = {}
ip = 0
out = []


def get_combo_value(operand):
    if 0 <= operand <= 3:
        return operand
    elif 4 <= operand <= 6:
        return {4: registers["A"], 5: registers["B"], 6: registers["C"]}[operand]
    raise Exception("Illegal combo")


def execute(operator, operand):
    global ip, out, registers
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


def evaluate(a=None):
    global ip, registers, out
    ip = 0
    out = []
    registers = {name[-1]: int(num) for name, num in [reg.split(": ")
                                                      for reg in inp[0].split("\n")]}
    if a is not None:
        registers["A"] = a

    while ip < len(instructions):
        operator = instructions[ip]
        operand = instructions[ip + 1]
        execute(operator, operand)
        ip += 2

    return out


print("p1:", ','.join([str(x) for x in evaluate()]))

a = 0
for i in range(len(instructions) - 1, -1, -1):
    a *= 2 ** 3
    output = evaluate(a)
    while output != instructions[i::]:
        a += 1
        output = evaluate(a)

print("p2:", a)
