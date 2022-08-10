#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


def dfs(here):
    visited[here] = True
    there = data[here]
    if not visited[there]:
        dfs(there)
    return 1

for _ in range(int(input())):
    input()
    res = 0
    data = list(map(lambda x: x - 1, MIS()))
    visited = [False for _ in range(len(data))]
    for node in range(len(data)):
        if visited[node]: continue
        res += dfs(node)
    print(res)