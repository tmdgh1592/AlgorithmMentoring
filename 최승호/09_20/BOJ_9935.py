#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline        

word, keyword = input().rstrip(), list(input().rstrip())
trigger, key_len = keyword[-1], len(keyword)

stack = []

for ch in word:
    stack.append(ch)
    if ch == trigger and len(stack) >= key_len:
        if stack[-key_len:] == keyword:
            for _ in range(key_len): stack.pop()
                
print(''.join(stack) if stack else 'FRULA')