from collections import defaultdict


lines = open("2023/dan10/in.txt").read().split("\n")
grid = []
visited = []

for line in lines:
    v = []
    grid.append(list(line))
    for i in range(len(line)):
        v.append(".")
    visited.append(v)


start = (0, 0)

grd = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
            grd[(i, j)].append((i + 1, j))
        elif grid[i][j] == "|":
            grd[(i, j)].append((i - 1, j))
            grd[(i, j)].append((i + 1, j))
        elif grid[i][j] == "-":
            grd[(i, j)].append((i, j - 1))
            grd[(i, j)].append((i, j + 1))
        elif grid[i][j] == "L":
            grd[(i, j)].append((i - 1, j))
            grd[(i, j)].append((i, j + 1))
        elif grid[i][j] == "J":
            grd[(i, j)].append((i - 1, j))
            grd[(i, j)].append((i, j - 1))
        elif grid[i][j] == "7":
            grd[(i, j)].append((i + 1, j))
            grd[(i, j)].append((i, j - 1))
        elif grid[i][j] == "F":
            grd[(i, j)].append((i + 1, j))
            grd[(i, j)].append((i, j + 1))
#print(start)
#print(grd)

q = []
stevec = 0
q.append(start)
prev = (start[0] + 1, start[1])
while len(q) > 0:
    cur = q.pop(0)
    if cur in grd and visited[cur[0]][cur[1]] == "." and cur[0] >= 0 and cur[0] < len(grid) and cur[1] >= 0 and cur[1] < len(grid[cur[0]]) and prev in grd[cur]:
        for i in grd[cur]:
            if i not in q:
                q.append(i)
        visited[cur[0]][cur[1]] = "#"
        stevec += 1
        prev = cur
for line in visited:
    for i in line:
        print(i, end="")
    print()
print(stevec/2)

            