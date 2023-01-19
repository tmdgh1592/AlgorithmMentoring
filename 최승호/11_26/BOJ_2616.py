#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def sub_sum(left, right):
    return prefix_sum[right] - prefix_sum[left - 1]

def f():
    


n = int(input())
data = list(MIS())
grep = int(input())
cache = []

prefix_sum = [0]
interval_sum = 0
for x in data:
    interval_sum += x
    prefix_sum.append(interval_sum)

print(f())