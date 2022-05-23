#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS() 
to_pick = sorted(list(MIS()))

def recursion(lst):
    if len(lst) == m:
        print(*lst)
        return None
    
    for there in to_pick:
        # if there not in lst and there > last_element:
        lst.append(there)
        recursion(lst)
        lst.pop()

recursion(list())