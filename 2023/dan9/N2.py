lines = open("2023/dan9/in.txt").read().split("\n")
rez = 0
for line in lines:
    
    line = line.split()   
    line = [int(x) for x in line]
    razlike = []
    while True:
        
        razlike.append(line)
        nova = []
        for i in range(len(line)-1):
            nova.append(line[i+1] - line[i])
        line = nova
        if all(x == 0 for x in nova):
            break
    razlike = razlike[::-1]
    st = 0
    print(razlike)
    for i, tab in enumerate(razlike):
        tab = tab[::-1]
        tab[-1] -= st
        st = tab[-1]
        if i == len(razlike)-1:
            rez += tab[-1]
        print(tab)
    print(razlike)
print(rez)
    
   