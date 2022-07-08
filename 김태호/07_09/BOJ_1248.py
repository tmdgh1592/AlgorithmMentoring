#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def is_possible(lst, t):
    tmp = 0
    k = t
    for i in range(k, -1, -1):
        tmp += lst[i]
        if sign_matrix[i][k] == 1 and tmp <= 0:
            return False
        elif sign_matrix[i][k] == -1 and tmp >= 0:
            return False
        elif sign_matrix[i][k] == 0 and tmp != 0:
            return False
    return True

def bf(cur_idx):
    if cur_idx == n:
        return True
    # print(cur_idx, seq, sign_matrix[cur_idx][cur_idx])
    if not sign_matrix[cur_idx][cur_idx]:
        seq[cur_idx] = 0
        return is_possible(seq, cur_idx) and bf(cur_idx + 1)
    
    else:
        for val in range(1, 11):
            # print('here', cur_idx)
            seq[cur_idx] = val * sign_matrix[cur_idx][cur_idx]
            if is_possible(seq, cur_idx) and bf(cur_idx + 1):
                return True

n = int(input())
lst = list(input())
sign_matrix = [[-1 for _ in range(n)] for _ in range(n)]
idx = 0
seq = [0 for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if lst[idx] == '-':
            sign_matrix[i][j] = -1
        elif lst[idx] == '+':
            sign_matrix[i][j] = +1
        else:
            sign_matrix[i][j] = 0
        idx += 1
        
# print(*sign_matrix, sep='\n')
bf(0)
print(*seq)