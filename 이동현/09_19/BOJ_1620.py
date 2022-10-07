from curses.ascii import isdigit
import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
pokemondict = defaultdict()

for i in range(n):
    pokemon = input().rstrip()
    pokemondict[pokemon] = i + 1
    pokemondict[i + 1] = pokemon

for i in range(m):
    p = input().rstrip()
    if p.isdigit():
        print(pokemondict[int(p)])
    else:
        print(pokemondict[p])