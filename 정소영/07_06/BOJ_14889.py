#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
lst = [list(MIS()) for _ in range(n)]

start = list()
link = list()

def calc(team):
    ret = 0
    for i in range(n // 2):
        for j in range(n // 2):
            if i == j: continue;
            ret += lst[team[i]][team[j]]
    return ret


