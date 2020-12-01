with open('input.txt') as file:
    nums = [int(x) for x in file.read().split('\n') if x]

for x in nums:
    for y in nums:
        if 2020 - x - y in nums:
            print(x * y * (2020 - x - y))
            