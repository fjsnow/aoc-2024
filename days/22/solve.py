with open("input", "r") as f:
    inp = [int(l.rstrip("\n")) for l in f.readlines()]


def price(a):
    return int(str(a)[-1])


def next_secret(s):
    s = (s ^ s * 64) % 16777216
    s = (s ^ s // 32) % 16777216
    s = (s ^ s * 2048) % 16777216
    return s


# p1
p1 = 0
for secret in inp:
    for _ in range(2000):
        secret = next_secret(secret)
    p1 += secret

# p2
global_seqs = {}
for secret in inp:
    secrets = [(secret, 0)]
    for i in range(1, 2000):
        last = secrets[i-1][0]
        next_ = next_secret(secrets[i-1][0])
        secrets.append((next_, price(next_) - price(last)))

    seqs = {}
    for i in range(len(secrets) - 3):
        four = secrets[i:i+4]
        if tuple([x[1] for x in four]) not in seqs:
            seqs[tuple([x[1] for x in four])] = price(four[-1][0])

    for seq, cost in seqs.items():
        global_seqs[seq] = global_seqs.get(seq, 0) + cost

print("p1:", p1)
print("p2:", max(list(global_seqs.values())))
