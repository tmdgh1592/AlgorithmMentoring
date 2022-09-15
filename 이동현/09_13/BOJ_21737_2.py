import code
import sys
import re
from collections import deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n  = int(input())

str = input().rstrip()

if 'C' not in str:
    print("NO OUTPUT")
    exit()

number = re.findall('[0-9]+', str)
number = deque(map(int, number))

oper = re.findall('[A-Z]',str)
oper = deque(oper)

def calc(oper, num1, num2):
    if oper == "S":
        return num1 - num2
    elif oper == "M":
        return num1 * num2
    elif oper == "U":
        if num1 < 0:
            num1 *= -1
            return -1 * (num1 // num2)
        else:
            return num1 // num2
    else:
        return num1 + num2

num = number.popleft()
for symbol in oper:
    if symbol == "C":
        print(num, end=" ")
    else:
        if len(number) > 0:
            num = calc(symbol, num, number.popleft())
            # print("rst = ", num)
        