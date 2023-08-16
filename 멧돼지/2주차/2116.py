import sys

n = int(sys.stdin.readline().rstrip())
dices = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
diceMap = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
ans = 0

for i in range(6):
    eachSum = 0
    top = 0
    bottom = 0
    for j in dices:
        k = j[:]
        if dices.index(j) == 0:
            top = k[i]
            bottom = k[diceMap[i]]
            k.remove(top)
            k.remove(bottom)
            eachSum += max(k)
        else:
            top = bottom
            bottom = k[diceMap[k.index(top)]]
            k.remove(top)
            k.remove(bottom)
            eachSum += max(k)
    if eachSum > ans:
        ans = eachSum

print(ans)
