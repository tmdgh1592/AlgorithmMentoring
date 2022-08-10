#-*- coding:utf-8 -*-
import sys
# 24891 문제
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


def dfs(cnt):
    if cnt == l:
        flag = True
        for i in range(l):
            for j in range(l):
                if res[i][j] != res[j][i]:
                    flag = False
        if flag:
            print(*res, sep='\n')
            exit(0)
        return None
        
    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        res[cnt] = data[i]
        dfs(cnt + 1)
        visited[i] = False
    return None

l, n = MIS()
data = sorted([input().rstrip() for _ in range(n)])
res = [0 for _ in range(l)]
visited = [False for _ in range(n)]
dfs(0)
print('NONE')
