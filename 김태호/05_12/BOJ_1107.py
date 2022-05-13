#-*- coding:utf-8 -*-
import sys


# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

target_channel = int(input())
num_broken = int(input())
lst = list(MIS())
broken_btn = [True if i in lst else False for i in range(10)]


def move_channel(to_channel):
    ret = 0
    
    if to_channel == 0:
        return not broken_btn[0]
    
    while to_channel > 0:
        if broken_btn[to_channel % 10]:
            return 0
        
        ret += 1
        to_channel //= 10
    
    return ret

res = abs(100 - target_channel)
for cur_channel in range(int(1e6)):
    tmp = move_channel(cur_channel)
    if tmp != 0:
        res = min(abs(target_channel - cur_channel) + tmp, res)

print(res)
