import queue

def neki(count,s):
    sprite = []
    for i in range(40):
        sprite.append(".")
    sprite[x - 1:x + 1] = "#" * 3
    if sprite[count % 40] == "#":
        s += "#"
    else:
        s += "."
    count += 1
    if count % 40 == 0:
        slika.append(s)
        s = ""
    return s,count

f = open("input.txt").read()
lines = f.split("\n")

x=1
count=0
commands=queue.Queue()
strength=0
b=0
slika=[]
sprite=[]
s=""

for line in lines:
    line=line.split(" ")
    commands.put(line)
while not commands.empty():
    command = commands.get()
    t=0
    if command[0] == "addx":
        for i in range(2):
            s, count = neki(count,s)
        x += int(command[1])
    else:
        s, count = neki(count,s)
for vrsta in slika:
    print(vrsta)



