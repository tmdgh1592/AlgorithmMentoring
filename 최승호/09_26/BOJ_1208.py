#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = list(MIS())
arr1, arr2 = arr[:n//2], arr[n//2:]

a, b = {}, {}
result = 0

for i in range(1, 1<<(len(arr1))):
    interval_sum = 0
    for j in range(len(arr1)):
        if i & 1 << j:
            interval_sum += arr1[j]
    if interval_sum in a:
        a[interval_sum] += 1
    else:
        a[interval_sum] = 1
for i in range(1, 1<<(len(arr2))):
    interval_sum = 0
    for j in range(len(arr2)):
        if i & 1 << j:
            interval_sum += arr2[j]
    if interval_sum == m:
        result += 1
    if m-interval_sum in a:
        result += a[m-interval_sum]

if m in a:
    result += a[m]
    
print(result)