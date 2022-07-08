#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


def prev_permutation(target_permutation):
    list_length = len(target_permutation)
    i = list_length - 1
    while i > 0 and target_permutation[i - 1] <= target_permutation[i]:
        i -= 1
    
    if i <= 0:
        print(-1)
        return None
    
    j = list_length - 1
    while target_permutation[j] >= target_permutation[i - 1]:
        j -= 1
    
    target_permutation[i - 1], target_permutation[j] = target_permutation[j], target_permutation[i - 1]

    j = list_length - 1
    while i < j:
        target_permutation[i], target_permutation[j] = target_permutation[j], target_permutation[i]
        i += 1
        j -= 1
    print(*target_permutation)

input()
prev_permutation(list(MIS()))
