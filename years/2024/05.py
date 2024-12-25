def meta():
    return {
        "title": "Print Queue",
        "solutions": {
            "a": 4924,
            "b": 6085
        }
    }

def parse(input):
    parts = [x.split("\n") for x in input.split("\n\n")]
    return (
        set([(rule.split("|")[0], rule.split("|")[1]) for rule in parts[0]]),
        [update.split(",") for update in parts[1]]
    )

def a(input):
    rules, updates = input

    a = 0
    for update in updates:
        log = set()
        for num in update:
            for num2 in log:
                if (num, num2) in rules:
                    break
            else:
                log.add(num)
                continue
            break
        else:
            a += int(update[len(update) // 2])

    return a

def b(input):
    rules, updates = input

    b = 0
    for update in updates:
        log = set()
        for num in update:
            for num2 in log:
                if (num, num2) in rules:
                    break
            else:
                log.add(num)
                continue
            break
        else:
            continue

        new = []
        for num in update:
            for li, l in enumerate(new):
                if (num, l) in rules:
                    new.insert(li, num)
                    break
            else:
                new.append(num)

        b += int(new[len(new) // 2])

    return b
