#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
eggs = [list(MIS()) for _ in range(n)]
res = 0

def get_broken_count():
    cnt = 0
    for i in range(n):
        if eggs[i][0] <= 0: cnt += 1
    return cnt

def hit(now):
    global res

    if now == n: res = max(res, get_broken_count()); return
    if eggs[now][0] <= 0: hit(now+1); return
    
    is_all_broken = True
    for i in range(n):
        if i != now and eggs[i][0] > 0:
            is_all_broken = False
            eggs[i][0] -= eggs[now][1]; eggs[now][0] -= eggs[i][1]
            hit(now + 1)
            eggs[i][0] += eggs[now][1]; eggs[now][0] += eggs[i][1]
    if is_all_broken: hit(n)

hit(0)
print(res)