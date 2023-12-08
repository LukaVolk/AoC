f = open("input.txt").read()
lines = f.split("\n")
rez = 0
for line in lines:
    maxColors={
        "red": 0,
        "blue": 0,
        "green": 0
    }
    possible = True
    id, its = line.split(": ")
    _, id = id.split(" ")
    its = its.split("; ")
    for it in its:
        colors = it.split(", ")
        for color in colors:
            num, colorName = color.split(" ")
            maxColors[colorName]= max(maxColors[colorName],int(num))
    rez += (maxColors["red"]*maxColors["green"]*maxColors["blue"])



print(rez)