def meta():
    return {
        "title": "Historian Hysteria",
        "solutions": {
            "a": 2970687,
            "b": 23963899
        }
    }

def parse(input):
    l, r = [], []
    for line in input.split("\n"):
        split = line.split()
        l.append(int(split[0]))
        r.append(int(split[1]))

    l.sort()
    r.sort()
    return (l, r)

def a(input):
    return sum(abs(le - re) for le, re in zip(input[0], input[1]))

def b(input):
    return sum(e * input[1].count(e) for e in input[0])
