#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e9))
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
INF = float('-inf')

def f(cnt, prev):
    if cnt + prev > total:
        return INF
    if cnt + prev == total:
        return 0
    if cache[cnt][prev] != -1:
        return cache[cnt][prev]

    cache[cnt][prev] = INF
    for score in scores:
        cache[cnt][prev] = max(cache[cnt][prev], f(cnt+score, cnt+prev) + score)
    
    return cache[cnt][prev]
    

for _ in range(int(input())):
    total, n = MIS()
    scores = list(MIS())
    cache = [[-1] * (total + 1) for _ in range(total+1)]
    
    res = f(0, 0)
    print(res if res > 0 else -1)