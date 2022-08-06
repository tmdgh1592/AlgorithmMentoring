import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m, p = MIS()
like_ch = []
hate_ch = []
for _ in range(n):
    like, hate = MIS()
    like_ch.append(like)
    hate_ch.append(hate)

visited = [False for _ in range(n)]

first_senior = hate_ch.index(p)
cnt = 0
while p in hate_ch:
    person = hate_ch.index(p)
    if cnt != 0 and first_senior == person:
        print(-1)
        exit()
    p = like_ch[person]
    cnt += 1
    
print(cnt)
