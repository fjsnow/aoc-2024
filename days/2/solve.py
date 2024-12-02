import sys

if len(sys.argv) > 1 and sys.argv[1] == "-r":
    with open("input", "r") as f:
        input = [l.rstrip("\n") for l in f.readlines()]
else:
    input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split("\n")

p1, p2 = 0, 0

# p1
for li, line in enumerate(input):
    nums = [int(n) for n in line.split(" ")]

    safe = True
    up = nums[1] > nums[0]
    for ni, num in enumerate(nums):
        if ni != 0:
            if (num > nums[ni-1] and not up) or abs(nums[ni-1] - num) < 1 or abs(nums[ni-1] - num) > 3:
                safe = False
        if ni != len(nums) - 1:
            if (num > nums[ni+1] and up) or abs(nums[ni+1] - num) < 1 or abs(nums[ni+1] - num) > 3:
                safe = False
        if not safe:
            break
    
    if safe:
        p1 += 1

# p2
for li, line in enumerate(input):
    nums = [int(n) for n in line.split(" ")]
    for i in range(len(nums)):
        copy = nums.copy()
        copy.pop(i)

        safe = True
        up = copy[1] > copy[0]
        for ni, num in enumerate(copy):
            if ni != 0:
                if (num > copy[ni-1] and not up) or abs(copy[ni-1] - num) < 1 or abs(copy[ni-1] - num) > 3:
                    safe = False
            if ni != len(copy) - 1:
                if (num > copy[ni+1] and up) or abs(copy[ni+1] - num) < 1 or abs(copy[ni+1] - num) > 3:
                    safe = False
            if not safe:
                break
        if safe:
            p2 += 1
            break

print("p1:", p1)
print("p2:", p2)
