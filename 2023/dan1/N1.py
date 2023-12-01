f = open("input.txt").read()
f = f.split("\n")
rez = 0
for line in f:
    any = 0
    first = 0
    last = -1
    for ch in line:
        if ch >= '0' and ch <= '9':
            if any == 0:
                first = ch
                any = 1
            else:
                last = ch
    if last == -1:
        last = first
    num = str(first) + str(last)
    rez += int(num)
print(rez)

