import re

with open("input.txt") as file:
    entries = file.read().split("\n\n")

passports = []

for entry in entries:

    passport = {}
    data = re.split("\\n| ", entry)
    for field in data:
        if ":" in field:
            key, value = field.split(":")
            passport[key] = value

    passports.append(passport)


def valid(passport):
    keys = list(passport.keys())
    keys.append("cid")
    return len(set(keys)) == 8


print(sum([valid(p) for p in passports]))
