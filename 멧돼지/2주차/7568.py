import sys

n = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
eachAns = 1
ans = []

for i in data:
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            eachAns += 1
    ans.append(eachAns)
    eachAns = 1

print(ans, sep="")

# 이거 틀린답인데 왜틀린지 모르겠어서 상의해봐야함 -> 출력 포멧이 안맞았다 난 병신 맞음