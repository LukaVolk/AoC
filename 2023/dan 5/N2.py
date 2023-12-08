def preveri(num, all):
    for a in all:
        if num >= a[0] and num <= a[1]:
            return True
    return False

groups = open("input.txt").read().split("\n\n")
_, seeds = groups[0].split(": ")
seeds = seeds.split()
seeds = [int(i) for i in seeds]
all = []

for i in range(len(seeds)//2):
    all.append((seeds[i*2], seeds[i*2+1] + seeds[i*2]-1))

rez = float('inf')
groups = groups[::-1]
stevec = 0

while True:
    num = stevec
    for group in groups[:-1]:
        group = group.splitlines()[1:]
        for line in group:
            count, start, length = line.split()
            count, start, length = int(count), int(start), int(length)

            if num >= count and num <= count+length:
                num = num - count + start
                break
    print(f"{stevec} / {num}")
    if preveri(num, all):
        print(f"Result: {stevec}")
        break
    stevec += 1