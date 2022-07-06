MIS = lambda: map(int, input().split())
L, C = MIS()
arr = sorted(list(input().split()))
vowel = ['a', 'e', 'i', 'o', 'u']


def password(sol, vowel_count, consonant_count):
    if len(sol) == L:
        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(sol))
        return None

    for i in range(C):
        if arr[i] in sol:
            continue
        if sol and max(sol) > arr[i]:
            continue
        sol.append(arr[i])
        if arr[i] in vowel:
            password(sol, vowel_count + 1, consonant_count)
        else:
            password(sol, vowel_count, consonant_count + 1)
        temp = sol.pop()

password(list(), 0, 0)