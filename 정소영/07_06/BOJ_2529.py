#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
ine_sign_arr = list(input().split(' '))

lst = []
visited = [False]*10

def check(ine_sign,a,b):

    if ine_sign =='<':
        return a < b
    if ine_sign == '>':
        return a > b

def func(idx, num):

    if idx == n + 1:
        lst.append(num)
        return

func(0, '')

print(lst[-1]) # 최대
print(lst[0])  # 최소
