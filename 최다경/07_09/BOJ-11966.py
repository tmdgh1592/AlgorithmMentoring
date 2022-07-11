n = int(input())
binary = bin(n)
zero = bin(0)
leng = len(binary)
cnt = 0
for i in range(3, leng):
    if binary[2] == '1' and binary[i] == '0':
        cnt += 1
if cnt == (leng - 3): print(1)
else: print(0)
