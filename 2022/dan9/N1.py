import numpy as np

def velikostMreze(moves):
    x, y = 1, 1
    xMax, yMax = 1, 1
    xMin, yMin = 1,1
    for move in moves:
        if move[0] == "R":
            x += int(move[1])
        elif move[0] == "L":
            x -= int(move[1])
        elif move[0] == "D":
            y -= int(move[1])
        elif move[0] == "U":
            y += int(move[1])
        if x > xMax:
            xMax = x
        if y > yMax:
            yMax = y
        if x < xMin:
            xMin = x
        if y < yMin:
            yMin = y
    #print(xMax, yMax)
    return xMax, yMax

def preveri(h, t):
    xh, yh = h[0], h[1]
    xt, yt = t[0], t[1]
    a=xh-xt
    b=yh-yt
    if a > 1:
        xt = xh-1
        yt = yh
    if a < -1:
        xt = xh+1
        yt = yh
    if b > 1:
        yt = yh-1
        xt = xh
    if b < -1:
        yt = yh + 1
        xt = xh

    return [xt,yt]

def premikanje(moves, mrezaVrv, MrezaHistory, x, y):
    h = [2500, 2500]
    t = [2500, 2500]
    mrezaVrv[h[0]][h[1]] = 1
    #print(mrezaVrv)
    for move in moves:
        for m in range(int(move[1])):
            if move[0] == "R":
                h[1] += 1
                t = preveri(h, t)
            elif move[0] == "L":
                h[1] -= 1
                t = preveri(h, t)
            elif move[0] == "D":
                h[0] += 1
                t = preveri(h, t)
            elif move[0] == "U":
                h[0] -= 1
                t = preveri(h, t)
            mrezaHistory[t[0]][t[1]] = 1
        #print(h)


f = open("input.txt").read()
f = f.split("\n")
moves = []
for move in f:
    move = move.split(" ")
    moves.append((move[0], move[1]))
x, y = velikostMreze(moves)
mrezaVrv = np.zeros((5000, 5000))
mrezaHistory = np.zeros((5000, 5000))
premikanje(moves, mrezaVrv, mrezaHistory, x, y)

st = np.count_nonzero(mrezaHistory == 1)
print(st)


