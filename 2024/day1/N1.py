# read input
f = open("Aoc/2024/day1/input.txt", "r")
input = f.read().split("\n")
f.close()

l1 = []
l2 = []
# split input into two lists
for line in input:
    x, y = line.split("   ")

    l1.append(int(x))
    l2.append(int(y))


# sort lists
l1.sort()
l2.sort()
# sum of diff
print(sum([abs(l1[i] - l2[i]) for i in range(len(l1))]))