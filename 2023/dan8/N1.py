direction, a = open("2023/dan8/in.txt").read().split("\n\n")
d = dict()
a = a.split("\n")
for i in a:
    start, tup = i.split(" = ")
    tup = tup[1:-1].split(", ")
    d[start] = tup
start = "AAA"
stevec = 0
while start != "ZZZ":
    smer = direction[stevec % len(direction)]
    if smer == "R":
        start = d[start][1]
    else:
        start = d[start][0]
    stevec += 1
print(stevec)

