import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
cnt = 0
devil = 666

while cnt != n:
    if '666' in str(devil):
        cnt += 1
    devil += 1
print(devil - 1)