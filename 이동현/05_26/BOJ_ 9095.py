# import sys
# sys.setrecursionlimit(10000)

# n = int(input())
# arr = []

# for i in range(n):
#     arr.append(int(input()))

# temp = []
# count = 0
# rst = []

# def decompose(index):
#     global count
#     if sum(temp) == arr[index]:
#         if ''.join(temp) in rst:
#             return None
#         else:
#             count += 1
#             print(temp)
#             rst.append(''.join(temp))
#         return None
    
#     for i in range(arr[index]):
#         num = i + 1
#         if i > 2:
#             num = 3
#         if sum(temp) + num > arr[index]:
#             continue
#         temp.append(num)
#         decompose(index)
#         temp.pop()

# for i in range(len(arr)):
#     decompose(i)
#     print(count)
#     count = 0
