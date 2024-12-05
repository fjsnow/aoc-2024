import re

with open("input", "r") as f:
    input = [l.rstrip("\n") for l in f.readlines()]

p1, p2 = 0, 0
enabled = True

for line in input:
    matches = re.findall(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)', line)
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don\'t()":
            enabled = False
        else:
            nums = [int(x) for x in re.findall(r'\d+', match)]

            value = nums[0] * nums[1]
            p1 += value
            if enabled:
                p2 += value

print("p1", p1)
print("p2", p2)
