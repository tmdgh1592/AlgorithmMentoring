#-*- coding:utf-8 -*-
import sys
from collections import Counter

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

size = int(input().rstrip())
array = [list(MIS()) for _ in range(size)]
arr1 = [0 for _ in range(size * size)]
arr2 = [0 for _ in range(size * size)]

for i in range(size):
    for j in range(size):
        arr1[i * size + j] = array[i][0] + array[j][1]
        arr2[i * size + j] = array[i][2] + array[j][3]

res = 0
counter = Counter(arr2)

for element in arr1:
    res += counter[-element]
print(res)