import queue

f = open("input.txt").read()
lines = f.split("\n")

x=1
count=0
commands=queue.Queue()
strength=0
b=0
maxX=0
for line in lines:
    line=line.split(" ")
    commands.put(line)
while not commands.empty():
    command = commands.get()
    t=0
    if command[0] == "addx":
        for i in range(2):
            count += 1
            if (count-20)%40 == 0:
                strength += x * count
        x += int(command[1])
        maxX = max(x,maxX)
    else:
        count += 1
        if (count - 20) % 40 == 0:
            strength += x * count
print(maxX)






