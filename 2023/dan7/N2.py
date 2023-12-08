from collections import Counter

lines = open("input.txt").read().split("\n")

slovar = {"A":"m","K":"l","Q":"k","T":"j","9":"i","8":"h","7":"g","6":"f","5":"e","4":"d","3":"c","2":"b","J":"a",}
rez = 0
d={
    "high":[], #5
    "one":[], #4
    "two":[], #3
    "three":[], #3
    "full":[], #2
    "four":[], #2
    "five":[], #1
}
game = dict()
for line in lines:
    cards, bet = line.split()
    l = []
    for i,card in enumerate(cards):
        l.append(slovar[card])
    cards = "".join(l)
    game[cards] = int(bet)
    counter = Counter(cards)
    if "a" not in counter:
        if len(counter) == 5:
            d["high"].append(cards)
        elif len(counter) == 4:
            d["one"].append(cards)
        elif len(counter) == 3:
            for item in counter:
                if counter[item] == 3:
                    d["three"].append(cards)
                    break
            else:
                d["two"].append(cards)
        elif len(counter) == 2:
            for item in counter:
                if counter[item] == 4:
                    d["four"].append(cards)
                    break
            else:
                d["full"].append(cards)
        else:
            d["five"].append(cards)
    elif counter["a"] == 1:
        if len(counter) == 5:
            d["one"].append(cards)
        elif len(counter) == 4:
            d["three"].append(cards)
        elif len(counter) == 3:
            for item in counter:
                if counter[item] == 3:
                    d["four"].append(cards)
                    break
            else:
                d["full"].append(cards)
        elif len(counter) == 2:
            d["five"].append(cards)
    elif counter["a"] == 2:
        if len(counter) == 4:
            d["three"].append(cards)
        elif len(counter) == 3:
            d["four"].append(cards)
        elif len(counter) == 2:
            d["five"].append(cards)
        else:
            d["five"].append(cards)
    elif counter["a"] == 3:
        if len(counter) == 3:
            d["four"].append(cards)
        if len(counter) == 2:
            d["five"].append(cards)
    elif counter["a"] == 4:
        d["five"].append(cards)
    else:
        d["five"].append(cards)
    a=0



all = []
for key in d:
    d[key].sort()
    all += d[key]
for i,c in enumerate(all):
    rez += (i+1)*game[c]
print(rez)

