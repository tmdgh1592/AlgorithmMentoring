#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 14)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(idx):
    if idx == n:
        res = 0
        
        for i in range(n):
            if data[i][0] <= 0:
                res += 1
        return res
    
    ret = 0
    
    if data[idx][0] <= 0:
        return max(f(idx + 1), ret)
        
    
    is_end = True
    
    for i in range(n):
        if i == idx: continue
        if data[i][0] > 0:
            is_end = False
            break
    
    if is_end:
        ret = max(n - 1, ret)
        
    for i in range(n):
        if idx == i: continue
        if data[i][0] <= 0: continue
        
        data[i][0] -= data[idx][1]
        data[idx][0] -= data[i][1]
        ret = max(f(idx + 1), ret)
        data[i][0] += data[idx][1]
        data[idx][0] += data[i][1]
    return ret

n = int(input())
data = [list(MIS()) for _ in range(n)]
print(f(0))