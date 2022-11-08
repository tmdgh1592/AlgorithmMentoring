import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = list(MIS())
print(n, m, arr)