import re


file = open("input.txt", "r")
input = file.read()


def part01(values):
    total = 1
    nums = re.findall(r"\d+", values)
    nums = [x for x in map(int, nums)]
    time = nums[0:3]
    distance = nums[4:8]
    for time, distance in zip(time, distance):
        wins = 0
        for hold in range(time):
            speed = hold * (time - hold)
            if speed > distance:
                wins += 1
        total *= wins
    return total


def part02(values):
    total = 1
    without_spaces = values.replace(" ", "")
    nums = re.findall(r"\d+", without_spaces)
    nums = [x for x in map(int, nums)]
    time = nums[0]
    distance = nums[1]
    wins = 0
    for hold in range(time):
        speed = hold * (time - hold)
        if speed > distance:
            wins += 1
    total *= wins
    return total


print(part01(input))
print(part02(input))
