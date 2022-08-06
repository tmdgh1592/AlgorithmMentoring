#틀렸습니다 ㄹㅇ 왜???
import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
number = list(MIS())
temp = []

def nasamgope():
    if len(temp) == n:
        print(*temp)
        return None
    for i in range(n):
        if len(temp) == 0 or (number[i] == temp[-1] * 2) or ((number[i] == (temp[-1] / 3)) and ((temp[-1] % 3 == 0))):
            temp.append(number[i])
            nasamgope()
            temp.pop()
nasamgope()