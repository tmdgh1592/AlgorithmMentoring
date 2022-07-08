#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def is_promising(arr):
    flag = True
    if len(arr) == 1: return True;
    
    for i in range(len(arr) - 1):
        if data[i] == '<':
            if arr[i] >= arr[i + 1]:
                flag = False;
                break;
        else:
            if arr[i] <= arr[i + 1]:
                flag = False;
                break;
            
    return flag;

def f(cnt, arr):
    if cnt == k + 1:
        res.append(''.join(arr))
        return None
    
    for i in range(10):
        if visited[i]: continue;
        visited[i] = True
        arr.append(str(i))
        if is_promising(arr): f(cnt + 1, arr);
        visited[i] = False
        arr.pop()

k = int(input())
data = input().rstrip().split()
visited = [False for _ in range(10)]
res = []
f(0, list())
res = sorted(res)
print(res[-1], res[0], sep='\n')
