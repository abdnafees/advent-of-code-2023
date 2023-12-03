import enum
import re


file = open('input.txt', 'r')
input = [i for i in file.read().strip('\n').split('\n')]

def part1(lines):
    total = 0
    for line in lines:
        numbers = re.findall(r'[0-9]', line)
        if len(numbers) == 1:
            double = f'{numbers[0]}{numbers[0]}' 
            total += int(double)
        else:
            total += int(numbers[0] + numbers[-1])
    return total

def part2(lines):
    wordstonum = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    def num(x: str):
        if x.isdigit():
            return x
        return wordstonum[x]
    
    pattern = "(?=(" + "|".join(wordstonum.keys()) + "|\\d))"
    ans = 0

    for line in lines:
        digits = re.findall(pattern,line)
        digits = [*map(num,digits)]
        ans += (int(f'{digits[0]}{digits[-1]}'))

    return (ans)


print(part2(input))
print(part1(input))