from collections import Counter

print("SA")
lines = open("2023/dan7/input.txt").read().split("\n")

slovar = {"A":"m","K":"l","Q":"k","J":"j","T":"i","9":"h","8":"g","7":"f","6":"e","5":"d","4":"c","3":"b","2":"a"}
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
    if len(counter) == 5:
        d["high"].append(cards)
    elif len(counter) == 4:
        d["one"].append(cards)
    elif len(counter) == 3:
        for item in counter:
            print(item)
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
all = []
for key in d:
    d[key].sort()
    all += d[key]
for i,c in enumerate(all):
    rez += (i+1)*game[c]
print(rez)

