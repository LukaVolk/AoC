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
        #razlike.append(nova)
        line = nova
        if all(x == 0 for x in nova):
            print(razlike)
            break
    razlike = razlike[::-1]
    print(razlike)
    st = 0
    for tab in razlike:
        tab[-1] = tab[-1] + st
        st = tab[-1]
    print(razlike)
    rez += razlike[-1][-1]
print(rez)
    
   