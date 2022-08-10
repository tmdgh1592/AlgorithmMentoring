#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs(idx, cur_cost):
    if idx >= n: return 0
    if cache[idx][cur_cost] != -1:
        return cache[idx][cur_cost]
    cache[idx][cur_cost] = dfs(idx + 1, cur_cost)
    if cost[idx] <= cur_cost:
        cache[idx][cur_cost] = max(memory[idx] + dfs(idx + 1, cur_cost - cost[idx]), cache[idx][cur_cost])
    return cache[idx][cur_cost]

n, m = MIS()
memory = list(MIS())
cost = list(MIS())
# cache[i][j] := i번째 앱까지 비용 j를 사용했을때의 메모리 최댓값
cache = [[-1 for _ in range(10001)] for _ in range(101)]
lo, hi = 0, sum(cost)

# 파라메트릭 서치

while lo < hi:
    mid = (lo + hi) // 2
    print(lo, mid, hi, dfs(0, mid))
    if m <= dfs(0, mid):
        hi = mid
    else:
        lo = mid + 1
        
print(lo)