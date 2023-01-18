#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def find_begin_number(row_or_col):
    if row_or_col <= 2: return 0
    elif row_or_col <= 5: return 3
    elif row_or_col <= 8: return 6

def check_row(row_number, col_number):
    cur_number = data[row_number][col_number]
    for col in range(9):
        if cur_number == data[row_number][col] and col_number != col: return False
    return True

def check_col(row_number, col_number):
    cur_number = data[row_number][col_number]
    for row in range(9):
        if cur_number == data[row][col_number] and row_number != row: return False
    return True

def check_square(row_number, col_number):
    begin_row = find_begin_number(row_number)
    begin_col = find_begin_number(col_number)
    cur_number = data[row_number][col_number]
    
    for i in range(3):
        for j in range(3):
            if cur_number == data[begin_row + i][begin_col + j] and row_number != begin_row + i and col_number != begin_col + j: return False
    return True

def checker(row_number, col_number):
    if check_row(row_number, col_number) and check_col(row_number, col_number) and check_square(row_number, col_number): return True
    return False

def f(idx):
    if idx == len(zeros):
        for d in data:
            print(*d)
        exit(0)

    for candi in range(1, 10):
        data[zeros[idx][0]][zeros[idx][1]] = candi
        if checker(zeros[idx][0], zeros[idx][1]):
            f(idx + 1)
    data[zeros[idx][0]][zeros[idx][1]] = 0
    return 

data = [list(MIS()) for _ in range(9)]
zeros = list()

for i in range(9):
    for j in range(9):
        if not data[i][j]:
            zeros.append((i, j))
            
f(0)
