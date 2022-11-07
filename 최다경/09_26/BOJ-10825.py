import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
arr = []
for _ in range(int(input())):
    n, k, e, m = input().rstrip().split()
    arr.append([n, int(k), int(e), int(m)])
arr.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])
