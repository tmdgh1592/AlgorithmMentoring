import code
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
nbs = list(MIS())
m = int(input())
qst = [0 for _ in range(m)]

def is_palin(s, e):
    cnt = 0
    #print("case start")
    for i in range(e - s):
        if nbs[s + i - 1] == nbs[e - i - 1]:
            #print("nbs", nbs[s + i - 1], nbs[e - i - 1])
            cnt += 1
    if cnt == (e - s):
        return True
    else: return False

for i in range(m):
    s, e = MIS()
    if is_palin(s, e):
        print(1)
    else: print(0)

