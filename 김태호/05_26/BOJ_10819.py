#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


def next_permutation(target_permutation):
    list_length = len(target_permutation)
    i = list_length - 1
    while i > 0 and target_permutation[i - 1] >= target_permutation[i]:
        i -= 1
    
    if i <= 0:
        return -1
    
    j = list_length - 1
    while target_permutation[j] <= target_permutation[i - 1]:
        j -= 1
    
    target_permutation[i - 1], target_permutation[j] = target_permutation[j], target_permutation[i - 1]

    j = list_length - 1
    # while i < j:
    #     target_permutation[i], target_permutation[j] = target_permutation[j], target_permutation[i]
    #     i += 1
    #     j -= 1
    target_permutation[i : ] = target_permutation[list_length - 1 : i - 1 : -1]
    return target_permutation

def my_permutation(arr):
    while type(arr) == list:
        yield arr
        arr = next_permutation(arr)

input()
given_list = sorted(list(MIS()))

res = -1

for data in my_permutation(given_list):
    tmp = 0
    for i in range(len(data) - 1):
        tmp += abs(data[i] - data[i + 1])
    res = max(tmp, res)
print(res)