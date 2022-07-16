#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def calc(lst):
    ret = 0
    
    for i in range(n // 2):
        for j in range(n // 2):
            if i == j: continue;
            ret += data[lst[i]][lst[j]]
    return ret

def get_diff(a, b):
    return abs(calc(a) - calc(b))


n = int(input())
data = [list(MIS()) for _ in range(n)]
res = float('inf')

for i in range(1 << n):
    cnt = 0
    for j in range(n):
        if i & (1 << j):
            cnt += 1
    
    if cnt != n // 2:
        continue
    
    team_a = list()
    team_b = list()
    
    for j in range(n):
        if i & (1 << j):
            team_a.append(j)
        else:
            team_b.append(j)

    tmp = get_diff(team_a, team_b)
    if tmp < res:
        res = tmp

print(res)
