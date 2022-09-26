import sys

input = sys.stdin.readline

MIS = lambda: map(int, input().rstrip().split())
a = []
b = []
c = []
d = []
arr = []
di = dict()
n = int(input())
for i in range(n):
    arr = list(MIS())
    a.append(arr[0])
    b.append(arr[1])
    c.append(arr[2])
    d.append(arr[3])

for i in a:
    for j in b:
        tmp = i + j
        if tmp not in di:
            di[tmp] = 0
        di[tmp] += 1
s = 0
for i in c:
    for j in d:
        tmp = i + j
        if -tmp in di:
            s += di[-tmp]


print(s)
