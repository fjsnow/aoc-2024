with open("input", "r") as f:
    input = "\n".join([l.rstrip("\n") for l in f.readlines()])

rulesStr, updatesStr = [p.split("\n") for p in input.split("\n\n")]
rules = [(rule.split("|")[0], rule.split("|")[1]) for rule in rulesStr]
updates = [update.split(",") for update in updatesStr]

p1, p2 = 0, 0
for i, update in enumerate(updates):
    log = []
    order = True
    for number in update:
        for l in log:
            if (number, l) in rules:
                order = False
                break
        log.append(number)
        if not order:
            break
    if order:
        p1 += int(update[len(update) // 2])
    else:
        log, new = [], []
        for number in update:
            for li, l in enumerate(new):
                if (number, l) in rules:
                    new.insert(li, number)
                    break
            else:
                new.append(number)

        p2 += int(new[len(new) // 2])

print("p1:", p1)
print("p2:", p2)

