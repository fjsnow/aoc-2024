def meta():
    return {
        "title": "Red-Nosed Reports",
        "solutions": {
            "a": 252,
            "b": 324
        }
    }

def parse(input):
    return [[int(x) for x in l.split(" ")] for l in input.split("\n")]

def a(input):
    s = 0
    for report in input:
        up = report[1] > report[0]
        for li, level in enumerate(report):
            if li != 0:
                below = report[li - 1]
                if (level > below and not up) or abs(below - level) < 1 or abs(below - level) > 3:
                    break
            if li != len(report) - 1:
                above = report[li + 1]
                if (level > above and up) or abs(above - level) < 1 or abs(above - level) > 3:
                    break
        else:
            s += 1

    return s

def b(input):
    s = 0

    for report in input:
        for i in range(len(report)):
            copy = report.copy()
            copy.pop(i)

            up = copy[1] > copy[0]
            for li, level in enumerate(copy):
                if li != 0:
                    below = copy[li - 1]
                    if (level > below and not up) or abs(below - level) < 1 or abs(below - level) > 3:
                        break
                if li != len(copy) - 1:
                    above = copy[li + 1]
                    if (level > above and up) or abs(above - level) < 1 or abs(above - level) > 3:
                        break
            else:
                s += 1
                break

    return s
