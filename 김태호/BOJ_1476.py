#-*- coding:utf-8 -*-
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

MAX_EARTH = 15
MAX_SUN = 28
MAX_MOON = 19

e, s, m = MIS()
earth, sun, moon = 1, 1, 1
res = 1

# def f(earth, sun, moon, cnt):
#     if earth == e and sun == s and moon == m:
#         # print(earth, sun, moon)
#         return cnt
#     # print(earth, sun, moon)
#     earth += 1
#     sun += 1
#     moon += 1
    
#     if earth > MAX_EARTH:
#         earth = 1
        
#     if sun > MAX_SUN:
#         sun = 1
        
#     if moon > MAX_MOON:
#         moon = 1
        
#     return f(earth, sun, moon, cnt + 1)

# res = f(1, 1, 1, 1)

while earth != e or sun != s or moon != m:
    earth += 1
    sun += 1
    moon += 1
    res += 1

    if earth > MAX_EARTH:
        earth = 1
        
    if sun > MAX_SUN:
        sun = 1
        
    if moon > MAX_MOON:
        moon = 1
        

print(res)
    
