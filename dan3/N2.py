with open('input.txt') as f:
    contents = f.read()
    vrstice = contents.split("\n")
    vsota = 0
    for i in range(0,int(len(vrstice)/3)):
        for znak in vrstice[i*3]:
            if znak in vrstice[i*3+1]:
                if znak in vrstice[i*3+2]:
                    if znak.isupper():
                        vsota += (ord(znak) - 38)
                    else:
                        vsota += (ord(znak) - 96)
                    break
print(vsota)


