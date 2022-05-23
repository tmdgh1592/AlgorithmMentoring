#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

ch = int(input())
num = int(input())
bt = list(MIS())
broken = [True if i in bt else False for i in range(10)]

def moveCh(ch):
    ret = 0

    if ch == 0:
        return not broken[0]


    while ch > 0 :
        if broken[ch % 10]:
            return 0
        
        ret += 1
        ch //= 10
    
    return ret

res = abs(100 - ch)

for curCh in range(int(1e6)):
    tmp = moveCh(curCh)

    if tmp != 0:
        res = min(res, abs(ch - curCh) + tmp)

print(res)






