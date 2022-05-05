n = 9
list = []
for i in range(n):
    list.append(int(input()))
SUM = sum(list)

for i in range(0,9):
    for j in range(0,9):
        if i != j:
            num1 = SUM - list[i] - list[j]
            if num1 == 100:
                a = i
                b = j
del list[a]
del list[b]
for i in list:
    print(i)