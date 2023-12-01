with open('input.txt') as f:
    contents = f.read()
    vrstice = contents.split("\n")
    vsota = 0
    for vrstica in vrstice:
        for znak in vrstica[:int(len(vrstica)/2)]:
            if znak in vrstica[int(len(vrstica)/2):]:
                if znak.isupper():
                    vsota += (ord(znak)-38)
                else:
                    vsota += (ord(znak) - 96)
                break
    print(vsota)

