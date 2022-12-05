with open('input.txt') as f:
    contents = f.read()
    vrstice = contents.split("\n\n")
    premiki = vrstice[1].split("\n")
    v = []
    stack = []

    posamezne = vrstice[0].split("\n")
    for x in posamezne:
        v += [row[1::4] for row in x.splitlines()]

    for j in range(0,len(v[0])):
        stack.append([])
        for i in range(len(v)-2,-1, -1):
            if v[i][j] != " ":
                stack[j].append(v[i][j])

    for premik in premiki:
        zac = []
        besede = premik.split(" ")
        for i in range(0,int(besede[1])):
            zac.append(stack[int(besede[3])-1].pop())
        for i in range(0,int(besede[1])):
            stack[int(besede[5])-1].append(zac.pop())
    s = ""
    for stolpec in stack:
        s += stolpec.pop()
    print(s)
