#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS() 
to_pick = sorted(list(MIS()))
visited = [False for _ in range(n)]

def recursion(lst):
    if len(lst) == m:
        print(*lst)
        return None
    
    last_element = -1
    
    for i in range(n):
        if visited[i]: continue;
        if last_element == to_pick[i]: continue;
        last_element = to_pick[i]
        visited[i] = True
        lst.append(to_pick[i])
        recursion(lst)
        visited[i] = False
        lst.pop()


recursion(list())
# print(total)

# import sys
# from collections import Counter

# sys.stdin = open('input.txt', 'r')
# n,m = map(int,input().split())
# temp = list(map(int,input().split()))
# temp = list(Counter(temp).items())
# temp.sort()
# n = len(temp)
# num,cnt = map(list,zip(*temp))

# a = [0]*m
# def go(index, n, m):
#     if index == m:
#         sys.stdout.write(' '.join(map(str,a))+'\n')
#         return
#     for i in range(n):
#         if cnt[i] > 0:
#             cnt[i] -= 1
#             a[index] = num[i]
#             go(index+1, n, m)
#             cnt[i] += 1
# go(0,n,m)
