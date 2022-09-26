#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

s = set()

for _ in range(int(input())):
    data = input().rstrip().split()
    
    if data[1][0] == 'e':
        s.add(data[0])
    else:
        s.remove(data[0])
        
print(*sorted(s, reverse=True), sep='\n')