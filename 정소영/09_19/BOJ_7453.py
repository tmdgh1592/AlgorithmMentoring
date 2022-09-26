#-*- coding:utf-8 -*-
from collections import Counter, defaultdict
from email.policy import default
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
A = list()
B = list()
C = list()
D = list()

for i in range(n):
    a, b, c, d, = MIS()
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
CD = []
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

cnt = Counter(CD)
res = 0

for i in AB:
    res += cnt[-i]
print(res)