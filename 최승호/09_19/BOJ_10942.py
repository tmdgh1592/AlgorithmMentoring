#-*- coding:utf-8 -*- 
import sys
  
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [0]+list(MIS())
d = [[False] * (n+1) for _ in range(n+1)]
m = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: d[i][j] = True

# s ~ e 사이의 숫자들은 모두 팰린드롬으로 갱신
def update(s, e):
    while s < e:
        if d[s][e]: return
        d[s][e] = True
        s += 1; e -= 1

# 팰린드롬 확인
def check(s, e):
    while s <= e:
        if arr[s] != arr[e]:
            return False
        else:
            if s+1 < n and e-1 > 0:
                if d[s+1][e-1]: return True
                else: s += 1; e -= 1
            else: break
    return True


for _ in range(m):
    s, e = MIS()
    flag = False

    if check(s, e):
        print(1)
        update(s, e)
    else: print(0)