#시간초과
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
    person = hate_ch.index(p) #person은 해당 채널을 싫어하는 사람
    if cnt != 0 and first_senior == person: # 만약 싫어하는 사람이 처음 채널을 바꾼 사람과 같다면 사이클 생성
        print(-1)
        exit()
    p = like_ch[person] # 채널을 person이 좋아하는 채널로 바꾼다.
    cnt += 1
    
print(cnt)
