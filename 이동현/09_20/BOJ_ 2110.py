import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, c = MIS()
home = list()

for _ in range(n):
    home.append(int(input()))

home = sorted(home)

lo = 1 #최소 거리는 1
hi = home[-1] - home[0] # 최대 거리는 가장 먼집에서 첫번째 집의 거리를 뺀 것이다.

def is_possible(dist):
    cnt = c - 1
    cur = home[0]#첫번째 집에는 무조건 설치(그리디)
    for i in range(1, n):
        if cur + dist <= home[i]:
            cur = home[i]# 공유기를 설치한 집으로 cur을 바꿈
            cnt -= 1
    if cnt > 0: #카운트를 모두 소진해야 참
        return False
    else:
        return True # 아니면 안됨

while lo <= hi:
    mid = (hi + lo) // 2
    
    if is_possible(mid):
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)