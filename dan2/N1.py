#A - kamen
#B - Papir
#C - skarje

#X - lose 0
#Y - draw 3
#Z - win 6

# Kamen 1
# papir 2
# skarje 3

vrednosti = {('B', 'Z'): 9,
             ('A', 'X'): 4,
             ('C', 'X'): 7,
             ('C', 'Z'): 6,
             ('A', 'Z'): 3,
             ('C', 'Y'): 2,
             ('B', 'Y'): 5,
             ('B', 'X'): 1,
             ('A', 'Y'): 8}

with open('input.txt') as f:
    contents = f.read()
    vsota = 0
    tab = contents.split("\n")
    tab.remove('')
    znaki = {(i[0], i[2]): tab.count(i) for i in tab}
    print(sum([int(vrednosti[x]) * int(znaki[x]) for x in znaki]))


