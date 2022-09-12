import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

for _ in range(n):
    s = list(input().split())
    for i in s:
        print(i[::-1], end = ' ')
    print()