with open('input.txt') as f:
    contents = f.read()
    vrstice = contents.split("\n")
    pari = []
    stevec = 0
    for x in vrstice:
        pari.append(x.split(","))
    for y in pari:
        prvi = y[0].split("-")
        drugi = y[1].split("-")
        a = set()
        b = set()
        for i in range(int(prvi[0]), int(prvi[1])+1):
            a.add(i)
        for i in range(int(drugi[0]), int(drugi[1])+1):
            b.add(i)
        if a - b != a:
            stevec += 1
    print(stevec)


