#-*- coding:utf-8 -*-
from curses.ascii import isdigit
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(input().rstrip())
res = 0

def calc(op, num1, num2):
    global res

    if op == 'S':
        return num1 - num2
    elif op == 'M':
        return num1 * num2
    elif op == 'U':
        if num1 < 0:
            return -(abs(num1) // num2)
        return num1 // num2
    elif op == 'P':
        return num1 + num2


nums = list()
ops = list()
answer = []
for i in arr:
    if isdigit(i):
        nums.append(int(i))
    else:
        ops.append(i)



if 'C' not in arr:
    print('NO OUTPUT')
else:
    for i in range(n - 1):
        if ops[i] == 'C':
            print(nums)
        else:
            res = calc(ops[i], nums[i], nums[i + 1])
            nums[i + 1] = res

