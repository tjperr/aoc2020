with open('q2/input.txt') as file:
    data = [x for x in file.read().split('\n') if x]

## Part 1
def valid(s):
    num, char, password = s.split(' ')
    min_num, max_num = num.split('-')
    min_num = int(min_num)
    max_num = int(max_num)
    char = char[0]

    if min_num <= password.count(char) <= max_num:
        return True
    return False

print(sum(valid(p) for p in data))

## Part 2
def valid2(s):
    num, char, password = s.split(' ')
    min_num, max_num = num.split('-')
    min_num = int(min_num)
    max_num = int(max_num)
    char = char[0]

    if (password[min_num-1] == char) + (password[max_num-1] == char) == 1:
        return True
    return False

print(sum(valid2(p) for p in data))