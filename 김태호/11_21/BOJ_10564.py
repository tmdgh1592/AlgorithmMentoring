#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(cumulated, total_score):
    if cumulated > n:
        return -float('inf')
    if cumulated == n:
        return total_score
    if cache[cumulated][total_score] != -1:
        return cache[cumulated][total_score]
    
    for score in data:
        cache[cumulated][total_score] = max(f(cumulated + total_score + score, total_score + score), cache[cumulated][total_score])
    return cache[cumulated][total_score]

for _ in range(int(input())):
    n, m = MIS()
    data = list(MIS())

    cache = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    res = f(0, 0)
    print(res if res != -float('inf') else -1)
    
    