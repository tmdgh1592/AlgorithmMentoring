#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS() 
to_pick = sorted(list(MIS()))
check = [False for _ in range(n)]

def recursion(lst):
    if len(lst) == m:
        print(*lst)
        return None
    
    last_element = -1
    
    for i in range(n):
        if check[i]: continue;
        if last_element == to_pick[i]: continue;
        if lst and lst[-1] > to_pick[i]: continue;
        last_element = to_pick[i]
        check[i] = True
        lst.append(to_pick[i])
        recursion(lst)
        check[i] = False
        lst.pop()


recursion(list())
