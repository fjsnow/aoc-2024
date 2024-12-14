from sympy import symbols, Eq, solve

with open("input", "r") as f:
    inp = f.read().rstrip("\n")

def parse(b):
    axes = b.split(": ")[1]
    x = int(axes.split(", ")[0][2:])
    y = int(axes.split(", ")[1][2:])
    return x, y

def do(claws, p2=False):
    sum = 0
    for claw in claws:
        a = parse(claw.split("\n")[0])
        b = parse(claw.split("\n")[1])
        prize = parse(claw.split("\n")[2])

        n, m = symbols('n m', integer=True)
        eq1 = Eq(a[0] * n + b[0] * m, (10e12 if p2 else 0) + prize[0]) 
        eq2 = Eq(a[1] * n + b[1] * m, (10e12 if p2 else 0) + prize[1])  
        solution = solve((eq1, eq2), (n, m))
        if solution != []:
            sum += solution[n] * 3 + solution[m]

    return sum

claws = inp.split("\n\n")
print("p1", do(claws, False))
print("p2", do(claws, True))
