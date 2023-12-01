
osnova=dict()
d=dict()
slovar={
    "=": 0,
    "-": 1,
    "0": 2,
    "1": 3,
    "2": 4
}

def napolni(l):
    osnova[0] = 0
    for i in range(22):
        d[i] = pow(5,int(i))
        osnova[i+1] = pow(5,int(i))*2+osnova[i]


def pretvori(line):
    first = line[0]
    dol = len(line)-1
    sum = osnova[dol]+1
    if first == "2":
        sum += d[dol]
    #obrni string
    line = line[::-1]
    for i, ch in enumerate(line[:-1]):
        sum += pow(5,i)*slovar[ch]
    return sum

def pretvoriNazaj(rez):
    i = 0
    prva = "1"
    st = ""
    while(rez > osnova[i]):
        i+=1
    rez -= osnova[i-1]+1
    if rez > d[i-1]:
        prva = "2"
        rez -= d[i-1]
    while(rez != 0):
        char = rez % 5
        char = list(slovar.keys())[list(slovar.values()).index(char)]
        rez //= 5
        st = str(char) + st
    if(len(st)<i-1):
        st = "=" + st
    st = prva + st
    return st


f = open("i.txt").read()
f = f.split("\n")
maxL = 0
rez=0
for line in f:
    l = len(line)
    if l > maxL:
        maxL = l
napolni(maxL)
for line in f:
    rez += pretvori(line)
result = pretvoriNazaj(rez)
print(result)
a=0


