mape = {}
path = ""
for line in open("input.txt").read().split("\n"):
    if "$ cd /" in line:
        path += "/"
    elif line == "$ cd ..":
        path = "/".join(path.split("/")[:-2])+"/"
    elif "$ cd" in line:
        path += line[5:] + "/"
    elif "$" not in line:
        typeOrSize, name = line.split()
        if typeOrSize != "dir":
            i = 0
            while "/" in path[i:]:
                i += path[i:].index("/") + 1
                if path[:i] in mape:
                    mape[path[:i]] += int(typeOrSize)
                else:
                    mape[path[:i]] = int(typeOrSize)
print(mape)
print(sum([mape[folder] for folder in mape if mape[folder]<100000])) # part 1

    #2.del
for m in sorted(mape.items(), key=lambda x: x[1]):
    if mape["/"] - int(m[1]) < 40000000:
        print(m[1])
        break