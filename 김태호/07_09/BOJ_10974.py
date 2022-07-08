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
    while i < j:
        target_permutation[i], target_permutation[j] = target_permutation[j], target_permutation[i]
        i += 1
        j -= 1
    return target_permutation

def my_permutation(n):
    _list = list(range(1, n + 1))
    while type(_list) == list:
        yield _list
        _list = next_permutation(_list)

for data in my_permutation(int(input())):
    print(*data)
