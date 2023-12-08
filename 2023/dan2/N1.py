omejitve={
    "blue": 14,
    "red": 12,
    "green": 13
}

f = open("input.txt").read()
lines = f.split("\n")
rez = 0
for line in lines:
    possible = True
    id, its = line.split(": ")
    _, id = id.split(" ")
    its = its.split("; ")
    for it in its:
        colors = it.split(", ")
        for color in colors:
            num, colorName = color.split(" ")
            if omejitve[colorName] < int(num):
                possible = False
                break
        if not possible:
            break
    if possible:
        rez += int(id)



print(rez)