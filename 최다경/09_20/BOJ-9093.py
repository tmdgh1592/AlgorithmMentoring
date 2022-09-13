import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

for i in range(n):
    for word in arr[i]:
        print(word[::-1], end = ' ')
    print()

