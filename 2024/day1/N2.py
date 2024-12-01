from collections import Counter
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


# count each number of occurences
c1 = Counter(l1)
c2 = Counter(l2)

print(sum([c1[key] * key * c2[key] for key in c1]))