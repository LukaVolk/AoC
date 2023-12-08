import re

def dotika(symbol, nums):
    xs, ys = symbol
    prva = 0
    druga = 0
    for st, x, start, end in nums:
        if x >= xs-1 and x <= xs+1 and end >= ys and start <= ys+1:
            if prva == 0:
                prva = st
            elif druga == 0:
                druga = st
            else:
                return prva * druga
    return prva * druga

f = open("input.txt").read()
lines = f.split("\n")
rez = 0
symbols = []
nums = []

for i, line in enumerate(lines):
    x = re.finditer("[*]", line)
    y = re.finditer("\d+", line)
    for match in x:
        symbols.append((i, match.start()))
    for match in y:
        nums.append((int(match.group()),i, match.start(), match.end()))
for symbol in symbols:
    rez += dotika(symbol, nums)

print(rez)
#[^\w\d.\n]

