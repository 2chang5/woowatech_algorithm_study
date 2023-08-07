# 기존에 그냥 브루트포스로 갈겼는데 사실 시간 복잡도 계산해보면 맞을수가 없는 문제임 문제가 잘못됨
# 그래서 백트래킹으로 푼건 사실 아니고 푸는방법 찾아봄(아직 백트래킹 어려움 그래도 풀다보니 재귀가 이해되기 시작)
# https://seongonion.tistory.com/98 이글 참고

import sys

n, s = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 0


def backTarcking(index, partSum):
    global ans

    if index >= n:
        return

    if (partSum + data[index]) == s:
        ans += 1

    backTarcking(index + 1, partSum + data[index])
    backTarcking(index + 1, partSum)


backTarcking(0, 0)
print(ans)

# 근데 다풀고 보니까 이것도 완전 탐색이지않나? 얼탱이없네
