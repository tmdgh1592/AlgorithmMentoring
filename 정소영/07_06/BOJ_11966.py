n = int(input())

if int((n & (n - 1)) == 0):
    print(1)
else:
    print(0)