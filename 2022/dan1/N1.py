with open('input.txt') as f:
    contents = f.read()
    skrati = contents.split("\n")
    vsota = 0
    kalorije = []
    for x in skrati:
        if x == "":
            kalorije.append(vsota)
            vsota = 0
        else:
            vsota += int(x)
    kalorije.append(vsota)
    print(max(kalorije))