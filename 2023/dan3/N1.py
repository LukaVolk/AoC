import re

def dotika(num, symbols):
    return any(x >= xs - 1 and x <= xs + 1 and end >= ys and start <= ys + 1 for xs, ys in symbols for st, x, start, end in [num])

lines = open("input.txt").read().split("\n")

symbols = [(i, match.start()) for i, line in enumerate(lines) for match in re.finditer("[^\w\d.\n]", line)]
nums = [(int(match.group()), i, match.start(), match.end()) for i, line in enumerate(lines) for match in re.finditer("\d+", line)]
rez=sum([num[0] for num in nums if dotika(num, symbols)])

print(rez)