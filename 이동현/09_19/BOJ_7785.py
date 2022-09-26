import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
company = defaultdict(int)

for _ in range(n):
    name, status = input().rstrip().split()
    if status == "enter":
        company[name] = 1
    if status == "leave":
        company[name] = 0

rst = sorted(company.keys(), reverse=True)

for i in rst:
    if company[i] == 1:
        print(i)