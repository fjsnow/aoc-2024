import re

def meta():
    return {
        "title": "Mull It Over",
        "solutions": {
            "a": 192767529,
            "b": 104083373
        }
    }

def parse(input):
    return input.split("\n")

def a(input):
    a = 0
    for line in input:
        matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        for match in matches:
            nums = [int(x) for x in re.findall(r'\d+', match)]
            a += nums[0] * nums[1]
    return a


def b(input):
    b, enabled = 0, True
    for line in input:
        matches = re.findall(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)', line)
        for match in matches:
            if match == "do()":
                enabled = True
            elif match == "don\'t()":
                enabled = False
            elif enabled:
                nums = [int(x) for x in re.findall(r'\d+', match)]
                b += nums[0] * nums[1]
    return b
