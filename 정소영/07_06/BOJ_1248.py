#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def is_possible(lst):
    k = len(lst) - 1
    res = 0
    for i in range(k, -1, -1): 
        res += arr[i]
        if sign_matrix[i][k] != 0 and res == 0:
            return False
        if sign_matrix[i][k] >= 0 and res <= 0:
            return False
        if sign_matrix[i][k] <= 0 and res >= 0:
            return False

    return True

def bf(lst):
    
    if len(lst) == n:
        if is_possible(lst):
            print(*lst)
        return None
    
    if sign_matrix[len(lst)][len(lst)] == 0:
        return None
    
    for val in range(1, 11):
        lst.append(val)
        if is_possible(lst):
            bf(lst)
        lst.pop()

n = int(input())
arr = list(input())
sign_matrix = [[-1 for _ in range(n)] for _ in range(n)]
idx = 0

for i in range(n):
    for j in range(i, n):
        if arr[idx] == '0':
            sign_matrix[i][j] = 0
            arr[idx] = 0
        elif arr[idx] == '+':
            sign_matrix[i][j] = 1
            arr[idx] = 1
        else:
            sign_matrix[i][j] = -1
            arr[idx] = -1
        idx += 1

bf(list())
