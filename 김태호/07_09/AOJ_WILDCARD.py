#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

# def match(w, s):
#     pos = 0
    
#     while pos < len(w) and pos < len(s) and (w[pos] == '?' or w[pos] == s[pos]):
#         pos += 1
        
#     if pos == len(w):
#         return pos == len(s)
    
#     if w[pos] == '*':
#         for skip in range(len(s) - pos + 1):
#             if match(w[pos + 1:], s[pos + skip:]):
#                 return TrueW
#     return False

# def match(w, s, W, S):
#     if cache[w][s] != -1:
#         return cache[w][s]
    
#     while s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
#         w += 1
#         s += 1
    
#     if w == len(W):
#         cache[w][s] = (s == len(S))
#         return cache[w][s]
    
#     if W[w] == '*':
#         for skip in range(len(S) - s + 1):
#             if match(w + 1, s + skip, W, S):
#                 cache[w][s] = 1
#                 return cache[w][s]
            
#     cache[w][s] = 0
#     return cache[w][s]

def match(w, s):
    if cache[w][s] != -1:
        return cache[w][s]
    
    if s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
        cache[w][s] = match(w + 1, s + 1)
        return cache[w][s]
    
    if w == len(W):
        cache[w][s] = (s == len(S))
        return cache[w][s]
    
    if W[w] == '*':
        if match(w + 1, s) or (s < len(S) and match(w, s + 1)):
            cache[w][s] = 1
            return cache[w][s]
            
    cache[w][s] = 0
    return cache[w][s]


for _ in range(int(input())):
    W = input().rstrip()
    res = []
    for s in [input().rstrip() for _ in range(int(input()))]:
        S = s
        cache = [[-1 for _ in range(101)] for _ in range(101)]
        if match(0, 0) == 1:
            res.append(s)
    print(*sorted(res), sep='\n')

