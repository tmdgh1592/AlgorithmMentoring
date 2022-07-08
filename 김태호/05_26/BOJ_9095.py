#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def count(n, cur_sum):
    if cur_sum > n:
        return 0
    if cur_sum == n:
        return 1
    
    ret = 0
    for cur_value in range(1, 4):
        ret += count(n, cur_sum + cur_value)
    
    return ret

for _ in range(int(input())):
    print(count(int(input()), 0))
