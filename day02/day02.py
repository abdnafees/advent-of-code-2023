import re


file = open('input.txt', 'r')
input = [i for i in file.read().strip('\n').split('\n')]


def part01(lines):
    total = 0
    for line in lines:
        id_game = line.split(':')
        game_id = id_game[0]
        num = re.findall(r'\d+', game_id)
        cubes = re.findall(r'(\d+\s\w+)', id_game[1])
        for cube in cubes:
            count, color = cube.split()
            if (color == 'red' and int(count) > 12 or color == "green" and int(count) > 13 or
            color == "blue" and int(count) > 14):
                break
        else:
            total += int(num[0])
    return total


def part02(lines):
    max_red = max_green = max_blue = sum = 0
    for line in lines:
        cubes = re.findall(r'(\d+\s\w+)', line)
        for cube in cubes:
            count, color = cube.split()
            if color == 'red' and int(count) > max_red:
                max_red = int(count)
            elif color == 'green' and int(count) > max_green:
                max_green = int(count)
            elif color == "blue" and int(count) > max_blue:
                max_blue = int(count)
        sum += max_red * max_green * max_blue
        max_red = max_green = max_blue = 0
    return sum

print(part01(input))
print(part02(input))