d={
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

f = open("input.txt").read()
f = f.split("\n")
rez = 0
for line in f:
    digits = []
    start = 0
    for i, c in enumerate(line):
        if c.isnumeric():
            digits.append(c)
            start = i
            continue

        for key in d:
            if key in line[start : i + 1]:
                digits.append(d[key])
                start = i
                break

    rez += int(digits[0] + digits[-1])

print(rez)

