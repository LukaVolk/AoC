import re

groups = open("i.txt").read().split("\n\n")
_, seeds = groups[0].split(": ")
seeds = seeds.split()
seeds = [int(i) for i in seeds]

rez = float('inf')
for seed in seeds:
    num = seed
    for group in groups[1:]:
        group = group.splitlines()[1:]
        for line in group:
            count, start, length = line.split()
            count, start, length = int(count), int(start), int(length)
            if num >= start and num <= start+length:
                num += count-start
                break
    rez = min(rez, num)


a=0