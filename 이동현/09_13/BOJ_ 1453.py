import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
number = list(MIS())

temp = set(number)

print(len(number)- len(temp))