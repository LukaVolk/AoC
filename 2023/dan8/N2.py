from math import lcm

direction, a = open("2023/dan8/in.txt").read().split("\n\n")
a = a.split("\n")
d = {i.split(" = ")[0]: i.split(" = ")[1][1:-1].split(", ") for i in a}
starts = [i for i in d if i[2] == "A"]

dolzine = []

for start in starts:
    stevec = 0
    while start[2] != "Z":
        smer = direction[stevec % len(direction)]
        if smer == "R":
            start = d[start][1]
        else:
            start = d[start][0]
        stevec += 1
    dolzine.append(stevec)

print(lcm(*dolzine)) 
