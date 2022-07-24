import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())



def dfs(y, x):
    visited[y][x] = True


    