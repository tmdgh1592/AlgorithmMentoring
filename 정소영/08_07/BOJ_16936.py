#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


n = int(input())
arr = list(MIS())

ans =[]

def dfs(num):

    if len(ans) == n:
        print(*ans)
        exit(0)

    if num % 3 == 0 and num // 3 in arr:
        ans.append(num // 3)
        dfs(num // 3)
        ans.pop()

    if num * 2 in arr:
        ans.append(num * 2)
        dfs(num * 2)
        ans.pop()
    
for i in arr:
    ans.append(i)
    dfs(i)
    ans.pop()
    