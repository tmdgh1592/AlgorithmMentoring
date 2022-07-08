#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(days, money):
    if days > len(data):
        return -1
    
    if days == len(data):
        return money
    
    ret = 0
    ret = max(f(days + 1, money), ret)
    ret = max(f(days + data[days][0], data[days][1] + money), ret)
    
    return ret

data = [list(MIS()) for _ in range(int(input()))]

print(f(0, 0))