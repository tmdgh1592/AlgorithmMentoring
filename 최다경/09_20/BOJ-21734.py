import sys

input = sys.stdin.readline
MIS = lambda: input().rstrip()

arr = list(MIS())

def s(num):
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res

for i in range(len(arr)):
    tmp = s(ord(arr[i]))
    print(arr[i] * tmp)

